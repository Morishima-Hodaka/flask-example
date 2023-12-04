# encoding: utf-8
# extensions/__init__.py
# 扩展模块
from flask import Flask
from .init_app_config import init_app_config

def init_plugs(app: Flask) -> None:
    init_app_config(app)


