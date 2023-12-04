# coding:utf-8
# application/init.py
import logging

from application.extensions import init_plugs
from application.views import init_view
from application.logs import init_logs
from flask import Flask

from config import config_map


# 工厂模式
def create_app(config_name='default'):
    """
    创建flask的应用对象
    :param config_name: str  配置模式的模式的名字 （"develop",  "product"）
    :return:
    """

    app = Flask(__name__)



    # 根据配置模式的名字获取配置参数的类
    app.config.from_object(config_map[config_name])

    # 注册各种插件
    init_plugs(app)

    # 注册蓝图 路由
    init_view(app)

    # 初始化日志
    init_logs(app)




    return app
