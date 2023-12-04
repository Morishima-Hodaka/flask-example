from flask import Flask
from flask_login import LoginManager

from app.models.more import User

"""
Flask-Login 是 Flask 的一个扩展，
提供了用户会话管理和认证功能。
它简化了处理用户登录、登出、用户会话的操作，同时提供了一些装饰器和函数，用于限制访问权限和处理用户认证。
"""


def init_login(app: Flask) -> None:
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.qeury.get(user_id)
