import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 用于加密会话数据等敏感信息的密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # 邮件服务器的主机名或IP地址
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    # 是否使用 TLS（传输层安全）协议。如果设置了环境变量 MAIL_USE_TLS 为 'true'、'on' 或 '1'（不区分大小写），则为 True，否则为 False
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
                   ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'

    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    #  管理员的邮箱地址。
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    # 数据库
    MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')

    SQLALCHEMY_DATABASE_URI = ("mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{"
                               "MYSQL_DATABASE}").format(MYSQL_USERNAME=MYSQL_USERNAME, MYSQL_PASSWORD=MYSQL_PASSWORD,
                                                         MYSQL_HOST=MYSQL_HOST, MYSQL_PORT=MYSQL_PORT,
                                                         MYSQL_DATABASE=MYSQL_DATABASE)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis
    REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)



    # 设置
    # 此设置对于任何Python项目都是通用的，不仅限于 Flask。
    DEBUG = os.environ.get('FLASK_DEBUG')

    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    # 项目路径
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

    # 日志路径
    LOG_PATH = os.path.join(PROJECT_PATH, 'logs')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_map = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
