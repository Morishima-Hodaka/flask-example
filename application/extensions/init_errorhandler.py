"""
`@app.errorhandler` 是 Flask 中的一个装饰器，Flask 是一个流行的 Python Web 框架。
它用于为在 Flask 应用程序执行过程中可能发生的特定 HTTP 错误代码或异常定义错误处理函数。
当在 Flask 应用程序中发生错误时，Flask 会自动寻找与特定错误代码或异常匹配的错误处理函数。
如果使用 `@app.errorhandler` 装饰器定义了这样的处理程序，Flask 将调用该函数来处理错误并生成适当的响应。
"""
import marshmallow
from flask import Flask, current_app, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from app.config import RET
from app.config.respone_code import error_map


def init_errorhandler(app: Flask) -> None:
    # @app.errorhandler(SQLAlchemyError)  # 捕捉 SQLAlchemyError 异常
    # def sql_alchemy_error(e):
    #     current_app.logger.debug("{}".format(e))
    #     print(e)
    #     return jsonify(RET=RET.DATAERR, msg=error_map[RET.DATAERR])



    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def validation_error(e):
        current_app.logger.debug("{}".format(e))
        return jsonify(RET=RET.PARAMERR, msg=error_map[RET.PARAMERR], e=e.messages)
