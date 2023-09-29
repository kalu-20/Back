from flask import Flask, jsonify, request
from config import Config
from flask_cors import CORS

from .routes.server_bp import server_bp
from .routes.user_bp import user_bp
from .routes.channel_bp import channel_bp
from .routes.message_bp import message_bp

from .routes.error_handlers import errors
from .database import DatabaseConnection

from .controllers.user_controller import UserController
from .controllers.server_controller import ServerController
from .controllers.channel_controller import ChannelController
from .controllers.message_controller import MessageController

def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    DatabaseConnection.set_config(app.config)

    CORS(app)

    @app.route('/app/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def api_users():
        if request.method == 'POST':
            data = request.json 
            return UserController.create_user(data)
        elif request.method == 'PUT':
            return UserController.modify_user(request.json)

    @app.route('/app/users/validate', methods=['POST', 'PUT'])
    def api_users_validate():
        if request.method == 'POST':
            return UserController.login_user(request.json)
        elif request.method == 'PUT':
            return UserController.pass_update(request.json)


    @app.route('/app/servers', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def api_servers():
        if request.method == 'GET':
            return ServerController.get_server_list()
        elif request.method == 'POST':
            data = request.json
            return ServerController.create_server(data)
    
    @app.route('/app/servers/<int:id_user>', methods=['GET'])
    def api_servers_user(id_user):
        return ServerController.get_servers_user(id_user)

        
    @app.route('/app/servers/findServer', methods=['POST'])
    def api_find_server():
        return ServerController.find_servers(request.json)

    @app.route('/app/servers/subscribir/', methods=['POST'])
    def api_servers_subscribir():
        return ServerController.subscribir(request.json)

    @app.route('/app/channels', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def api_channels():
        if request.method == 'POST':
            return ChannelController.create_channel(request.json)

    @app.route('/app/channel/channelByServer/<int:id_server>', methods=['GET'])
    def api_channel_by_server(id_server):
        return ChannelController.get_channels_server(id_server)

    @app.route('/app/messages', methods=['GET', 'POST', 'PUT'])
    def api_messages():
        if request.method == 'POST':
            return MessageController.create_message(request.json)
        elif request.method == 'PUT':
            return MessageController.modify_message(request.json)
    
    @app.route('/app/messages/<int:id_message>/<int:id_user>', methods=['DELETE'])
    def api_delete_messages(id_message, id_user):
        return MessageController.delete_message(id_message, id_user)

    @app.route('/app/messages/<int:id_channel>', methods=['GET'])
    def api_messages_channel(id_channel):
        return MessageController.get_message_list(id_channel)

    if __name__ == '__main__':
        app.run()

    return app
