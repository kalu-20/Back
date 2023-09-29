from flask import Blueprint
from ..controllers.message_controller import MessageController

message_bp = Blueprint('message_bp', __name__)


# Crear un nuevo usuario
message_bp.route('/', methods=['POST'])(MessageController.create_message)
message_bp.route('/<int:id_channel>', methods=['GET'])(MessageController.get_message_list)
