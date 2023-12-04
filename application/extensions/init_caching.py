from flask import Flask
from flask_caching import Cache

"""
lask-Caching 是 Flask 的一个扩展，
提供了缓存功能的支持。通过 Flask-Caching，
你可以方便地在 Flask 应用程序中使用缓存，提高应用性能，
减少对数据库或其他外部资源的访问次数。
"""


def init_caching(app):
    config = {'CACHE_TYPE': 'simple'}
    # 配置缓存
    cache = Cache(app, config=config)
