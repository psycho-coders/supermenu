from flask import Blueprint
from .menu import menu_handler

v1_app = Blueprint("v1", __name__, url_prefix="/v1")

@v1_app.route("/")
def health():
    return "OK"

v1_app.register_blueprint(menu_handler)