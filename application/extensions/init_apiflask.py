from apiflask import APIBlueprint, APIFlask

"""
APIFlask 是一个基于Flask和marshmallow-code项目的轻量级 Python Web API 框架。
它易于使用、高度可定制、与 ORM/ODM 无关，并且与 Flask 生态系统 100% 兼容。
pip install apiflask
 https://apiflask.com/
"""


bp = APIBlueprint('foo', __name__)
def init_apiflask(app):
    api = APIFlask(__name__)


