from flask import Flask
from flask_mail import Mail

"""
Flask-Mail 是 Flask 的一个扩展，
它提供了方便的邮件发送功能。使用 Flask-Mail，
你可以在 Flask 应用中发送电子邮件，例如用户注册欢迎邮件、密码重置邮件等
"""
mail = Mail()


def init_mail(app: Flask):
    mail.init_app(app)

