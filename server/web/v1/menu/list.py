from . import menu_handler
from pkg.models.menu.menu import Menu

@menu_handler.route("/list")
def list():
    m=Menu("1", None)
    m.get()
    return m.data if m.data is not None else "Not Found\n"
