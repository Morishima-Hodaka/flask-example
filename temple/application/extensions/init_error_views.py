from flask import jsonify, current_app
from sqlalchemy.exc import SQLAlchemyError

from app.config.respone_code import RET, error_map


def init_error_views(app):
    pass
    # @app.errorhandler(403)
    # def page_not_found(e):
    #     return jsonify(''), 403

    # @app.errorhandler(404)
    # def page_not_found(e):
    #     return jsonify(''), 404

    # @app.errorhandler(500)
    # def internal_server_error(e):
    #     return jsonify(''), 500

    # @app.errorhandler(SQLAlchemyError)
    # def sql_alchemy_error(e):
    #     current_app.logger.debug("{}".format(e))
    #     return jsonify(RET=RET.DATAERR, msg=error_map[RET.DATAERR])
