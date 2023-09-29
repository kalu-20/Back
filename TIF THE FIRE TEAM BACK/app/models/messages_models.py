from ..database import DatabaseConnection
from .exceptions import DatabaseError, UserNotFound 
from datetime import datetime

class Messages:

    def __init__(self, id_message = None, id_user = None, id_channel = None, content = None ,
        creation = None, username = None, profile_image = None):
        self.id_message = id_message
        self.id_user = id_user
        self.id_channel = id_channel
        self.content = content
        self.creation = creation
        self.username = username
        self.profile_image = profile_image
        
    def to_dict(self):
        return {
            'id_message': self.id_message,
            'id_user': self.id_user,
            'id_channel': self.id_channel,
            'content': self.content,
            'creation': self.creation,
            'username': self.username,
            'profile_image': self.profile_image
        }
    
    @classmethod
    def get_message_list(cls, id_channel):
        query = """SELECT m.id_message, m.id_user, m.id_channel, m.content, m.creation, u.username, u.profile_image FROM messages as m, users as u WHERE id_channel = %s AND u.id_user = m.id_user"""
        params = (id_channel,)
        results = DatabaseConnection.fetch_all(query, params=params)

        messages_list = []
        for result in results:
            message = Messages(
                id_message=result[0],
                id_user=result[1],
                id_channel=result[2],
                content=result[3],
                creation=result[4],
                username=result[5],
                profile_image=result[6],
            )
            messages_list.append(message.to_dict()) 
        return messages_list

    @classmethod
    def create_message(cls, msj):
        try: 
            query = """INSERT INTO messages (id_user, id_channel, content, creation) VALUES (%s, %s, %s, %s)"""
            params = (msj.id_user, msj.id_channel, msj.content, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            cursor = DatabaseConnection.execute_query(query, params)
            return 200
        except Exception as e: 
            return "Error " + str(e)

    @classmethod
    def create_channel(cls, channel):
        query = """INSERT INTO channels (id_server, name)
            VALUES (%s, %s)"""
        params = channel.name, channel.id_server
        cursor = DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def modify_message(cls, message):
        query = """UPDATE messages SET content = %s WHERE id_user = %s AND id_message = %s"""
        params = message.content, message.id_user, message.id_message
        print(params)
        cursor = DatabaseConnection.execute_query(query, params=params)

        if(cursor.rowcount == 1):
            return {"msg": "200"}, 200
        return {"msg": "403"}, 403


    @classmethod
    def delete_message(cls, id_message, id_user):
        query = """DELETE FROM messages WHERE id_message = %s AND id_user = %s"""
        params = (id_message,id_user)
        cursor = DatabaseConnection.execute_query(query, params=params)
        if(cursor.rowcount == 1):
            return {"msg": "200"}, 200
        return {"msg": "403"}, 403
        
    