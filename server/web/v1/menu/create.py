from . import menu_handler
from pkg.models.menu.menu import Menu


@menu_handler.route("/create")
def create():
    Menu("1", "first", "<body> </body").create()
    return "created"
