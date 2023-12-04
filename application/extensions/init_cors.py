from flask import Flask
from flask_cors import CORS

"""
处理 Flask 应用程序中跨域资源共享（Cross-Origin Resource Sharing，简称 CORS）的扩展。
CORS 是一种浏览器安全机制，用于限制跨域请求。
当你的前端应用程序（例如使用 JavaScript）试图从不同的域名、端口或协议发送请求时，浏览器会执行 CORS 检查，以确定是否允许该请求
"""


def init_cors(app: Flask):
    # 你的应用将能够接受跨源请求，并且可以携带认证凭据
    CORS(app, supports_credentials=True)
