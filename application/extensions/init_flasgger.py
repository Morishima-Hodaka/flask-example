from flask import Flask
from flasgger import Swagger

"""
Flask-Flasgger 是一个用于集成 Swagger UI 到 Flask 应用中的扩展。
Swagger UI 是一个用于构建、设计和测试 RESTful API 的工具。

Flask-Flasgger 提供了一个简单的方式来编写 API 文档，并将其与 Flask 应用集成。
它允许您使用装饰器和注释来定义 API 路由和参数，并自动生成 Swagger UI 页面，以便开发人员可以浏览和测试 API。
"""


def init_flasgger(app: Flask):
    # 写接口文档用
    # 初始化Swagger，配置Swagger的基础路径和应用信息
    app.config['SWAGGER'] = {
        'title': '硅基API',
        'version': '1.0.0',
        'base_path': 'https://api.guijichanye.com',
        'specs_route': '/traffic/apidocs/'
    }
    swagger = Swagger(app)
