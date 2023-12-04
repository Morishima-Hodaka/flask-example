from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
Flask-SQLAlchemy 是一个用于在 Flask 应用程序中使用 SQLAlchemy 的扩展。
SQLAlchemy 是一个功能强大的 Python ORM（对象关系映射）库，
它提供了一种将数据库表和 Python 对象进行映射的方式，使开发人员能够使用 Python 代码来操作数据库，而不必直接与 SQL 语句交互。

"""

db = SQLAlchemy()
# 设置 expire_on_commit=False
# 创建会话时设置 expire_on_commit 参数为 False，以禁用自动过期（expire）已提交（committed）的对象
db.session.expire_on_commit = False


def init_sqlalchemy(app: Flask):
    db.init_app(app)

