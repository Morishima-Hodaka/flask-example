
"""
Redis（Remote Dictionary Server）
是一个开源的，基于内存的数据结构存储系统，通常被用作缓存、消息中间件，以及数据存储
"""
import redis
from flask import Flask
# redis_client = redis.Redis(host='127.0.0.1', port=6379)

sms_redis_client = redis.Redis(
        host='127.0.0.1',
        port=6379,
        db=0
    )
def init_redis(app: Flask):
    pass









