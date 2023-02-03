from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask("server")
    CORS(app)
    from .v1 import v1_app
    app.register_blueprint(v1_app, url_prefix="/v1")

    return app
