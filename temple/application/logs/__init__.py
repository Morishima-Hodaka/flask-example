# encoding: utf-8
# logs/__init__.py
import logging

from flask import Flask


# 类型注解
def init_logs(app: Flask):
    app.logger.info("gunicorn 重启")
    # 配置日志输出到屏幕

    # 将日志输出到 gunicorn 中
    # 获取指定名称的 Logger，如果不存在则创建
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
