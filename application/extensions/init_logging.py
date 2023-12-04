import logging

from flask import Flask
from logging.handlers import TimedRotatingFileHandler

"""
Flask-Logging 是一个 Flask 扩展，用于增强 Flask 应用的日志功能。
它提供了更加灵活和强大的日志配置选项，可以帮助开发者更好地管理和处理应用的日志信息。
"""


def init_logging(app: Flask) -> None:
    # 按照日志大小切分
    # handler = RotatingFileHandler("flask.log", maxBytes=1024000, backupCount=10)
    # 按照日期进行切分
    # handler = TimedRotatingFileHandler(
    #     "flask.log", when="D", interval=1, backupCount=15,
    #     encoding="UTF-8", delay=False, utc=True)
    #
    # handler.setLevel(logging.DEBUG)
    #
    # # 创建一个格式化器，用于定义日志的格式
    # formatter = logging.Formatter('[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s')
    # handler.setFormatter(formatter)
    #
    # # 记录重启
    # app.logger.info("gunicorn 重启")
    # # 这行代码用于向 Flask 应用程序的日志处理器列表中添加一个新的日志处理器
    # app.logger.addHandler(handler)

    # # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    #
    # file_log_handler = RotatingFileHandler('log', maxBytes=1024 * 1024 * 100,
    #                                        backupCount=10)  # maxBytes=1024*1024*100  = 100M ,backupCount=10 最多10个100M
    #

    # # 为刚创建的日志记录器设置日志记录格式
    # file_log_handler.setFormatter(formatter)
    # # 为全局的日志工具对象（flask app使用的）添加日记录器
    # logging.getLogger().addHandler(file_log_handler)
    #
    app.logger.setLevel(logging.DEBUG)
    # 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
    formatter = logging.Formatter(
        '%(asctime)s,%(levelname)s,%(filename)s,%(lineno)d,%(message)s')  # 2020-06-08 09:57:46,536:ERROR user_cli_ds_look.py:1161 division by zero

    sh = logging.handlers.RotatingFileHandler("flask666.log", maxBytes=1024000, backupCount=10)
    # sh = logging.StreamHandler()  # 往屏幕上输出
    sh.setFormatter(formatter)  # 设置屏幕上显示的格式

    sh.setLevel(logging.DEBUG)
    app.logger.addHandler(sh)












