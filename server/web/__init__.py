from flask import Flask


def create_app():
    app = Flask("server")

    from .v1 import v1_app
    app.register_blueprint(v1_app, url_prefix="/v1")

    return app
