from flask import request, jsonify
from ..models.messages_models import Messages

class MessageController:
    
    @classmethod
    def get_message_list(cls, id_channel):
        return {'message': Messages.get_message_list(id_channel)}, 200

    @classmethod
    def create_message(cls, data):
        msj = Messages(
            id_user=data.get('id_user'),
            id_channel=data.get('id_channel'),
            content=data.get('content')
        )
        return {'message': Messages.create_message(msj)}, 200 

    @classmethod
    def modify_message(cls, data):
        msj = Messages(
            id_user=data.get('id_user'),
            id_message=data.get('id_message'),
            content=data.get('content')
        )
        return Messages.modify_message(msj)

    @classmethod
    def delete_message(cls, id_message, id_user):
        return {'message': Messages.delete_message(id_message, id_user)}, 200 