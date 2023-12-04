"""
app.config是一个用于配置Flask应用程序的对象或字典
它用于存储应用程序的配置变量，例如数据库连接信息、密钥、调试模式
"""


def init_app_config(app) -> None:
    # 模板文件夹设置
    app.template_folder = "/test/guiji/dist"
    # 静态文件夹设置
    app.static_folder = "/test/guiji/dist/static"
    app.static_url_path = '/'
    # 设置 JSON 使用 UTF-8 编码
    app.config['JSON_AS_ASCII'] = False
