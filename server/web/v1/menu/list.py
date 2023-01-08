from . import menu_handler
from pkg.models.menu.menu import Menu

@menu_handler.route("/list")
def list():
    return Menu("id", "1").get("id")
