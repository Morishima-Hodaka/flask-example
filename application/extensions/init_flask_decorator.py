"""
在 Flask 中，装饰器是一种用于修改或扩展函数行为的特殊语法。
装饰器允许你在不修改原始函数代码的情况下，通过将其包装在另一个函数中来添加额外的功能。

"""

from flask import Flask, request, g, session

from app.extensions.init_jwt import token_required


def init_flask_decorator(app: Flask) -> None:
    pass

    @app.before_request
    def before_request():
        print("before_request")
        print(request.path)
        print(request.method)

        headers = request.headers
        content_type = headers.get("Content-Type")
        method = request.method

        if method == "POST" and content_type != "multipart/form-data":
            g.data = request.get_json()
            if "token" in g.data:
                session["phone"] = g.data["token"]

        if method == "GET":
            g.data = request.args
            g.page = request.args.get("page", 1)
            g.size = request.args.get("size", 10)
        if method == "PATCH":
            g.data = request.get_json()
        if method == "DELETE":
            g.data = request.get_json()

    # @mini_admin_bp.before_request
    # def before_request():
    #
    #     method = request.method
    #     if method == "POST":
    #         g.data = request.get_json()
    #         try:
    #             token = g.data["token"]
    #             phone = token_required(token)
    #             session["phone"] = phone
    #
    #         except Exception as e:
    #             print(e)
    #
    #     if method == "GET":
    #         g.data = request.args
    #         try:
    #             token = g.data["token"]
    #             phone = token_required(token)
    #             session["phone"] = phone
    #
    #         except Exception as e:
    #             print(e)
    #
    #     if method == "PATCH":
    #         g.data = request.get_json()
    #         try:
    #             token = g.data["token"]
    #             phone = token_required(token)
    #             session["phone"] = phone
    #
    #
    #         except Exception as e:
    #             print(e)
    #     if method == "DELETE":
    #
    #         g.data = request.get_json()
    #         try:
    #             token = g.data["token"]
    #             phone = token_required(token)
    #             session["phone"] = phone
    #         except Exception as e:
    #             print(e)
