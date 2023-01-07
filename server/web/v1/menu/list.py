from . import menu_handler


@menu_handler.route("/list")
def list():
    return "list"
