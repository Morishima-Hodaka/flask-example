import os
from flask import Flask
import redis
from flask_session import Session


"""
flask-Session 是 Flask 的一个扩展，
用于管理用户会话（sessions）。它允许你在 Flask 应用中存储和访问用户会话数据，
以便在不同请求之间保持用户的状态信息。会话通常用于存储用户登录状态、购物车内容、用户偏好设置等
"""


def init_session(app: Flask):
    app.config["SESSION_COOKIE_NAME"] = b"session_cookie".decode("utf-8")
    #
    app.config['SESSION_TYPE'] = 'redis'  # 指定会话存储类型为 Redis
    # app.config['SESSION_PERMANENT'] = False  # 设置会话是否长期有效
    # app.config['SESSION_USE_SIGNER'] = True  # 对会话 cookie 进行签名
    # app.config['SESSION_KEY_PREFIX'] = 'your_prefix_'  # 会话键名前缀
    # app.config['SESSION_REDIS'] = redis.StrictRedis(host='localhost', port=6379,
    #                                                 db=0)  # 配置 Redis 连接信息，host 为 Redis 服务器地址，port 为端口号，db 为 Redis 数据库编号
    Session(app)




