from flask import Flask
from .v1 import v1_app

app = Flask("server")

app.register_blueprint(v1_app, url_prefix="/v1")