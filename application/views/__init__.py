# encoding: utf-8
# 视图模块
# views/__init__.py
from flask import Flask


# 类型注解
def init_view(app: Flask):
    app.register_blueprint(phone_bp)
    app.register_blueprint(index_bp)



