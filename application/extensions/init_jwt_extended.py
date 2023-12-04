"""
Flask-JWT-Extended 是 Flask 中处理 JSON Web Tokens（JWT）的强大扩展，
WT（JSON Web Token）
是一种用于在网络上安全地传输信息的开放标准（RFC 7519）。
JWT 是一种紧凑的、自包含的方式，用于在各方之间作为 JSON 对象安全地传输信息。
"""
from flask import Flask
from flask_jwt_extended import JWTManager

jwt = JWTManager()


def init_jwt(app: Flask):
    jwt.init_app(app)
