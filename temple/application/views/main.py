import logging

from flask import Blueprint, current_app, render_template

index_bp =Blueprint('index', __name__, url_prefix='')


@index_bp.route('/')
def index():
    current_app.logger.info("Hello World!")

    return "1"

    # return render_template("index.html")
