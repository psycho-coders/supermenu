import json

import pkg.models.menu.menu as menu

from . import menu_handler


@menu_handler.route("/list/<creator>")
def list(creator):
    print(creator)
    res = menu.all(creator)
    return json.dumps({"result": [d.__dict__ for d in res]})
