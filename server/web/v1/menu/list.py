from . import menu_handler
from pkg.models.menu.menu import Menu

@menu_handler.route("/list")
def list(): 
    m=Menu("1", "<body> </body").get()
    return m.data
