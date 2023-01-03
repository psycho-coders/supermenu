from flask import Blueprint

menu_handler = Blueprint("menu", __name__)

@menu_handler.route("/create")
def create():
    return "created"