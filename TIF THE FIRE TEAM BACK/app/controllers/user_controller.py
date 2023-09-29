from flask import request, jsonify
from ..models.user_model import Users

class UserController:

    @classmethod
    def create_user(cls, data):
        user = Users(
            email=data.get('email'),
            username=data.get('user'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            password=data.get('password'),
            birth_date=data.get('birth_date'),
            profile_image=""
        )

        Users.create_user(user)
        
        user_dict = user.to_dict()
        
        return {'message': user_dict}, 200

    @classmethod
    def modify_user(cls, data):
        user = Users(
            id_user=data.get('id_user'),
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            profile_image = data.get('profile_image')
        )
        return Users.modify_user(user)

    @classmethod
    def login_user(cls, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Ingrese correo y contraseña"}), 400

        query = """SELECT * FROM users WHERE email = %s AND password = %s"""
        params = (email, password)

        user = Users.authenticate_user(query, params)

        if user:
            return jsonify({"user": user.to_dict()}), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404

    
    @classmethod
    def get_users(cls):
        users = Users.get_user()
        users_members = []
        for user in users:
            users_members.append(user.__dict__)
            
        return  users_members, 200  

    @classmethod
    def pass_update(cls, data):
        user = Users(
            id_user=data.get('id_user'),
            password=data.get('password')
        )
        return Users.pass_update(user)
    
    @classmethod
    def get_by_id(cls, id_user):
        user_obj = Users(id_user=id_user)
        user = Users.get_user(user_obj)
        if user:
            return user.__dict__, 200

    @classmethod 
    def update_user(cls, user):
        data = request.json
        user = Users(
            id_user=data.get('id_user'),
            email=data.get('email'),
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            password=data.get('password'),
            birth_date=data.get('birth_date'),
            profile_image=data.get('profile_image')
        )
        Users.update_user(user)
        
        return {'message': 'Usuario modificado exitosamente'}, 200
   
   #cambio de contraseña ver si esta correcta la consulta###############################
    @classmethod 
    def update_password(cls, user):
        data = request.json
        if data.get('newPassword')==data.get('confirmNewPassword'):
            user= user.get_user(cls, data.get('id_user'))
            if user['password']==data.get('password'):
                Users.update_password(user(data.get('id_user'), password=data.get('newPassword')))
                return {'message': 'Contraseña modificado exitosamente'}, 200
            else:
                return {'message': 'La contraseña anterior no es valida'}, 404 #########ver error          
        else:
            return {'message': 'Las nueva contraseña y la confirmación no son iguales'}, 404 #########ver error  
        
    @classmethod
    def delete_user(cls, user):
        data = request.json
    
    
    
    
    
    
        
    #      @classmethod
    # def update_pasword (cls, pasword, newpasword,confirmnewpasword):
    #     if newpasword == confirmnewpasword:
    #         Users.update_pasword (cls,pasword,newpasword)
    #     else:
    #         return {'message': 'Las contraseñas no son iguales'},#buscar error#####################

    #no es necesario este metodo, porque no se lo va a utilizar
    # @classmethod
    # def delete_user(cls, id_user):
    #     user_obj = Users(id_user=id_user)
    #     Users.delete_user(user_obj)
    #     return {'message': 'Usuario eliminado exitosamente'}, 200
