from ..database import DatabaseConnection
from .exceptions import DatabaseError,  UserNotFound

class Servers:

    def __init__(self, id_server = None, name = None, description = None):
        self.id_server = id_server
        self.name = name
        self.description = description
    
    def to_dict(self):
        return {
            'id_server': self.id_server,
            'name': self.name,
            'description': self.description
        }

    def to_dict_list(self):
        return [Servers.to_dict() for server in self.servers]
    
    @classmethod
    def create_server(cls, server, id_user):
        query = """INSERT INTO servers (name, description)
            VALUES (%s, %s)"""
        params = server.name, server.description
        cursor = DatabaseConnection.execute_query(query, params=params)
    
        query = """INSERT INTO user_server (id_user, id_server)
            VALUES (%s, %s)"""
        params = id_user, cursor.lastrowid
        cursor2 = DatabaseConnection.execute_query(query, params=params)

        if cursor.rowcount == 1 and cursor2.rowcount == 1:
            server_id = cursor.lastrowid
            return server_id
        else:
            raise DatabaseError("No se pudo crear el nuevo servidor")

    @classmethod
    def subscribir(cls, id_server, id_user):
        query = """SELECT * FROM user_server WHERE id_user = %s AND id_server = %s"""
        params = id_user, id_server
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return "Error"
        else:
            query = """INSERT INTO user_server (id_user, id_server)
                VALUES (%s, %s)"""
            cursor = DatabaseConnection.execute_query(query, params=params)
            if cursor.rowcount == 1:
                server_id = cursor.lastrowid
                return server_id
            else:
                raise DatabaseError("No se pudo vincular al nuevo servidor")



    @classmethod
    def get_server(cls, server):
        query = """SELECT server_id, server_name, description
            FROM servers
            WHERE server_id = %s"""
        params = server.server_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return Servers(
                    server_id = result[0],
                    server_name = result[1],
                    description = result[2]
                )
        else:
            raise serverNotFound("El server solicitado no existe")

    @classmethod
    def get_server_list(cls):
        query = """SELECT id_server, name, description FROM servers"""
        results = DatabaseConnection.fetch_all(query)
        server_list = []
        for result in results:
            server = Servers(
                id_server=result[0],
                name=result[1],
                description=result[2]
            )
            server_list.append(server.to_dict()) 
        return server_list
    
    @classmethod
    def get_servers_user(cls, id_user):
        query = """SELECT s.id_server, s.name, s.description FROM servers as s, user_server as u WHERE s.id_server = u.id_server AND u.id_user = %s"""
        params = (id_user,)
        results = DatabaseConnection.fetch_all(query, params=params)
        server_list = []
        for result in results:
            server = Servers(
                id_server=result[0],
                name=result[1],
                description=result[2]
            )
            server_list.append(server.to_dict()) 
        return server_list

    @classmethod
    def find_servers(cls, data):
        name = data['name'] 
        query = """SELECT id_server, name, description FROM servers WHERE name LIKE %s"""
        params = ('%' + name + '%',) 
        results = DatabaseConnection.fetch_all(query, params=params)
        
        server_list = []
        for result in results:
            id_server, name, description = result  # Desempaqueta los valores de la tupla
            server = Servers(
                id_server=id_server,
                name=name,
                description=description
            )
            server_list.append(server.to_dict()) 
        
        return server_list


#     @classmethod
#     def delete_server(cls, server):
#         query = """DELETE FROM servers WHERE server_id = %s"""
#         params = server.server_id,
#         cursor = DatabaseConnection.execute_query(query, params=params)

#         if cursor.rowcount == 0:
#             raise DatabaseError("No se pudo eliminar el servidor")
#         else:
#             return {"message": "Servidor eliminado con éxito"}
    
#     @classmethod
#     def update_server(cls, server):
#         query = "UPDATE servers SET "
#         server_data = server.__dict__
#         server_values = []
#         server_updates = []
#         for key in server_data.keys():
#             if key != "server_id" and server_data[key] is not None:
#                 server_updates.append(f"{key} = %s")
#                 server_values.append(server_data[key])
#         query += ", ".join(server_updates)
#         query += " WHERE server_id = %s"
#         server_values.append(server.server_id)
#         params = tuple(server_values)
#         DatabaseConnection.execute_query(query, params=params)