# encoding: utf-8
# wsgi.py
# 项目的启动文件 gunicorn wsgi:app
from application import create_app
from dotenv import load_dotenv

# 加载环境变量
load_dotenv(dotenv_path=".env")
# 创建应用
app = create_app()
