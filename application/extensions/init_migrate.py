from flask import Flask
from flask_migrate import Migrate
"""
Flask-Migrate 是一个用于数据库迁移管理的 Flask 扩展，
它基于 Alembic，提供了在 Flask 应用中进行数据库迁移的功能。
数据库迁移是指在数据库模型发生变化时，通过一系列步骤使数据库的结构和数据保持同步的过程。
"""


from app.extensions import db

def init_migrate(app: Flask):
    migrate = Migrate(app, db)
    # render_as_batch=True, # 比较默认值
    # compare_type=True,# compare_type默认为False,不检测数据变化
    # compare_server_default=True # default默认约束的生成
    # migrate.init_app(app, db, Migrate(app, db, render_as_batch=True, compare_type=True, compare_server_default=True))

