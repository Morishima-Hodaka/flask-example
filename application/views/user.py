from application.utils.db_tool import *
from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/')
def index():
    pass

