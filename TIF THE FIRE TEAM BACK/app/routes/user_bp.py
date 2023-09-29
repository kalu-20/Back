from flask import Blueprint
from ..controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)


# Crear un nuevo usuario
user_bp.route('/', methods=['POST'])(UserController.create_user)
user_bp.route('/validate', methods=['POST'])(UserController.login_user)


# Obtener un usuario por su ID
user_bp.route('/users/<int:id_user>', methods=['GET'])(UserController.get_by_id)

# Obtener todos los usuarios (posiblemente por categoría)
user_bp.route('/users', methods=['GET'])(UserController.get_users)

# Actualizar un usuario por su ID
user_bp.route('/users/<int:id_user>', methods=['PUT'])(UserController.update_user)

# Eliminar un usuario por su ID
user_bp.route('/users/<int:id_user>', methods=['DELETE'])(UserController.delete_user)
