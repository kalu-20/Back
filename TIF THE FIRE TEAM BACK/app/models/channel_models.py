from ..database import DatabaseConnection
from .exceptions import DatabaseError, UserNotFound ######VER SI ES USER O POR CADA MODELO UN EXCEPTION

class Channels:

    def __init__(self, id_channel = None, id_server = None, name = None, description = None ):
        self.id_channel = id_channel
        self.id_server = id_server
        self.name = name
        self.description = description
        
    def to_dict(self):
        return {
            'id_channel': self.id_channel,
            'id_server': self.id_server,
            'name': self.name,
            'description': self.description
        }
    
    @classmethod
    def get_channel_list(cls):
        query = """SELECT * FROM channels"""
        results = DatabaseConnection.fetch_all(query)
        channel_list = []
        for result in results:
            channel = Channels(
                id_channel=result[0],
                id_server=result[1],
                name=result[2],
                description=result[3]
            )
            channel_list.append(channel.to_dict()) 
        return channel_list

    @classmethod
    def get_channels_server(cls, id_server):
        query = """SELECT id_channel, id_server, name, description
            FROM channels
            WHERE id_server = %s"""
        params = (id_server,)
        results = DatabaseConnection.fetch_all(query, params=params)
        
        channels_list = []
        for result in results:
            channel = Channels(
                id_channel=result[0],
                id_server=result[1],
                name=result[2],
                description=result[3]
            )
            channels_list.append(channel.to_dict()) 
        return channels_list


    @classmethod
    def create_channel(cls, channel):
        query = """INSERT INTO channels (id_server, name)
            VALUES (%s, %s)"""
        params = channel.id_server, channel.name
        cursor = DatabaseConnection.execute_query(query, params=params)

        if cursor.rowcount == 1:
            server_id = cursor.lastrowid
            return channel.id_server
        else:
            raise DatabaseError("No se pudo crear el nuevo canal")
        
#     @classmethod
#     def delete_channel(cls, channel):
#         query = """DELETE FROM channels WHERE id_channel = %s"""
#         params = channel.id_channel,
#         cursor = DatabaseConnection.execute_query(query, params=params)

#         if cursor.rowcount == 0:
#             raise DatabaseError("No se pudo eliminar el canal")##########################################VER!!!!!!
#         else:
#             return {"message": "Canal eliminado con éxito"}
    
#     @classmethod
#     def update_channel(cls, channel):
#         query = "UPDATE channels SET "
#         channel_data = channel.__dict__
#         channel_values = []
#         channel_updates = []
#         for key in channel_data.keys():
#             if key != "channel_id" and channel_data[key] is not None:
#                 channel_updates.append(f"{key} = %s")
#                 channel_values.append(channel_data[key])
#         query += ", ".join(channel_updates)
#         query += " WHERE channel_id = %s"
#         channel_values.append(channel.id_channel)
#         params = tuple(channel_values)
#         DatabaseConnection.execute_query(query, params=params)