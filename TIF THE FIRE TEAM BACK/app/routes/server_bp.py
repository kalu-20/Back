from flask import Blueprint
from ..controllers.server_controller import ServerController

server_bp = Blueprint('server_bp', __name__)


# Crear un nuevo usuario
server_bp.route('/', methods=['POST'])(ServerController.create_server)
server_bp.route('/<int:id_user>', methods=['GET'])(ServerController.get_servers_user)
server_bp.route('/', methods=['GET'])(ServerController.get_server_list)
