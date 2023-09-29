from ..database import DatabaseConnection
from .exceptions import DatabaseError, UserNotFound
from flask import request

class Users:

    def __init__(self, id_user = None, email = None, username = None, first_name = None, last_name = None,  password = None, birth_date = None, profile_image = None ):
        self.id_user = id_user
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.birth_date = birth_date
        self.profile_image = profile_image
    
    def to_dict(self):
        return {
            'id_user': self.id_user,
            'email': self.email,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'profile_image': self.profile_image,
            'password': self.password
        }

    @classmethod
    def authenticate_user(cls, query, params):
        cursor = None
        user = None

        try:
            cursor = DatabaseConnection.get_connection().cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            for result in results:
                print(result)
            if results:
                user_data = {
                    'email': result[0],
                    'id_user': result[1],
                    'username': result[2],
                    'first_name': result[3],
                    'last_name': result[4],
                    'password': result[5],
                    'birth_date': result[6],
                    'profile_image': result[7]
                }
                user = Users(**user_data)
        except Exception as e:
            print("Error en la autenticación:", str(e))    
        finally:
            if cursor:
                cursor.close()  
        return user

    @classmethod
    def pass_update(cls, user):
        query = """UPDATE users as u SET u.password = %s WHERE u.id_user = %s"""
        params = (user.password, user.id_user)  
        cursor = DatabaseConnection.execute_query(query, params)
        print(cursor)

        if cursor.rowcount == 1:
            query = """SELECT id_user, email, username, first_name, last_name, password, birth_date, profile_image
                FROM users
                WHERE id_user = %s"""
            params = user.id_user,
            result = DatabaseConnection.fetch_one(query, params=params)
            if result is not None:
                user_result = Users(
                        id_user = result[0],
                        email = result[1],
                        username = result[2],
                        first_name = result[3],
                        last_name = result[4],
                        password = result[5],
                        birth_date = result[6],
                        profile_image = result[7] 
                    )
                print(user_result.to_dict())
                return {"msj":user_result.to_dict()}, 200  
        else: 
            return {"msg": "201"}, 201 

    @classmethod
    def get_user(cls, user):
        
        """Método de clase que devuelve una tupla con todos los datos de usuario definidos en la Clase"""
        
        query = """SELECT id_user, email, username, first_name, last_name, password, birth_date, profile_image
            FROM users
            WHERE id_user = %s"""
        params = user.id_user,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return Users(
                    id_user = result[0],
                    email = result[1],
                    username = result[2],
                    first_name = result[3],
                    last_name = result[4],
                    password = result[5],
                    birth_date = result[6],
                    profile_image = result[7] 
                ),200
        return {"msj":"No se encontró el usuario"}, 404            
    
    
    @classmethod
    def create_user(cls, user):
        query = """INSERT INTO users (email, username, first_name, last_name, password, birth_date, profile_image)
            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        params = (user.email, user.username,user.first_name, user.last_name, user.password, user.birth_date, user.profile_image,)  
        cursor = DatabaseConnection.execute_query(query, params)
        
        return {"msg": "Usuario creado con éxito"}, 201

    @classmethod
    def modify_user(cls, user):
        query = """UPDATE users SET username = %s, first_name = %s, last_name = %s, email = %s, profile_image = %s WHERE id_user = %s"""
        params = (user.username, user.first_name, user.last_name, user.email, user.profile_image, user.id_user)  
        cursor = DatabaseConnection.execute_query(query, params)
        print(cursor.rowcount)
        
        if cursor.rowcount == 1:
            query = """SELECT id_user, email, username, first_name, last_name, password, birth_date, profile_image
                FROM users
                WHERE id_user = %s"""
            params = user.id_user,
            result = DatabaseConnection.fetch_one(query, params=params)
            if result is not None:
                user_result = Users(
                        id_user = result[0],
                        email = result[1],
                        username = result[2],
                        first_name = result[3],
                        last_name = result[4],
                        password = result[5],
                        birth_date = result[6],
                        profile_image = result[7] 
                    )
                print(user_result.to_dict())
                return {"msj":user_result.to_dict()}, 200  
        else: 
            return {"msg": "400"}, 201

        
    
    
    #modifica la contraseña
    @classmethod 
    def update_password(cls,user):
        query = "UPDATE users SET password = %s WHERE id_user = %s;"
        params= (user.password, user.id_user)
        DatabaseConnection.execute_query(query, params)
   
        return {"msg": "Contraseña actualizada con éxito"}, 200
    
    #EN ESTE PROYECTO, NO LO VAMOS A UTILIZAR , YA QUE ESTA ACCION ELIMINARIA EL USUARIO. 
    # @classmethod
    # def delete_user(cls, id_user):
    #     query = """DELETE FROM users WHERE id_user = %s"""
    #     params = id_user,
    #     cursor = DatabaseConnection.execute_query(query, params)

    #     if cursor.rowcount == 0:
    #         raise DatabaseError("No se pudo eliminar al usuario")
    #     else:
    #         return {"message": "Usuario eliminado con éxito"}
    # 
    # 
    # 
    # 
    # 
    # #metodo de clase que devuelve una lsita de todos los usuarios , es necesaria?
    # @classmethod
    # def get_user_list(cls):
    #     query = """SELECT id_user, email, username, first_name, last_name, pasword, birth_date, profile_image
    #     FROM users"""
    #     results = DatabaseConnection.fetch_all(query)
    #     user_list = []
    #     for result in results:
    #         user_list.append(Users(
    #             id_user = result[0],
    #             email = result[1],
    #             username = result[2],
    #             first_name = result[3],
    #             last_name = result[4],
    #             pasword = result[5],
    #             birth_date = result[6],
    #             profile_image = result[7]
    #         ))
    #     return user_list 
    