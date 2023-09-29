from flask import request, jsonify
from ..models.channel_models import Channels

class ChannelController:
    
    @classmethod
    def get_channels_server(cls, id_server):
        return {'message': Channels.get_channels_server(id_server)}, 200

    @classmethod
    def create_channel(cls, data):
        channel = Channels(
            name=data.get('name'),
            id_server=data.get('id_server')
        )
        
        return {'message': Channels.create_channel(channel)}, 200

    @classmethod
    def get_channel_list(cls):
        return {'message': Channels.get_channel_list()}, 200       