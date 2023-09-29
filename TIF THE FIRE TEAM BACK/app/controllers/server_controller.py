from flask import request, jsonify
from ..models.server_models import Servers
import json

class ServerController:

    @classmethod
    def create_server(cls, data):
        server = Servers(
            name=data.get('server_name'),
            description="",
        )
        Servers.create_server(server, data.get('id_user'))
        server_dict = server.to_dict()
        return {'message': server_dict}, 200

    @classmethod
    def subscribir(cls, data):
        return {'message': Servers.subscribir(data.get('id_server'), data.get('id_user'))}, 200

    @classmethod
    def get_server_list(cls):
        servers = Servers.get_server_list()
        return {'message': servers}, 200

    @classmethod
    def get_servers_user(cls, id_user):
        servers = Servers.get_servers_user(id_user)
        return {'message': servers}, 200

    @classmethod
    def find_servers(cls, name):
        servers = Servers.find_servers(name)
        return {'message': servers}, 200