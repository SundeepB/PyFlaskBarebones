from flask import Blueprint

barebones = Blueprint('barebones', __name__)

from . import views
