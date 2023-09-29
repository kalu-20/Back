from flask import Blueprint
from ..controllers.channel_controller import ChannelController

channel_bp = Blueprint('channel_bp', __name__)


# Crear un nuevo usuario
channel_bp.route('/', methods=['POST'])(ChannelController.create_channel)
channel_bp.route('/', methods=['GET'])(ChannelController.get_channel_list)
channel_bp.route('/channelByServer/<int:id_server>', methods=['GET'])(ChannelController.get_channels_server)
