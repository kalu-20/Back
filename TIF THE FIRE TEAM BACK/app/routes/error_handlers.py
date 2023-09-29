from flask import Blueprint
from ..models.exceptions import *

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(UserNotFound)
def handle_user_not_found(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(DatabaseError)
def handle_database_error(error):
    return error.get_response(), error.status_code