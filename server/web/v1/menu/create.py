from . import menu_handler
from pkg.models.menu.menu import Menu
from flask import Flask, json, request

@menu_handler.route("/create", methods=['POST'])
def create():
    menu_details = request.get_json()
    try: 
        Menu(menu_details['creator'], menu_details['name'], menu_details['sections']).create()
        return "created"
    except Exception as err:
        return "error"

