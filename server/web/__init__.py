from flask import Flask
from .v1 import v1_handler

app = Flask("server")

app.register_blueprint(v1_handler, url_prefix="/v1")