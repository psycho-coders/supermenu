from flask import Blueprint

menu_handler = Blueprint("menu", __name__)

from . import create
