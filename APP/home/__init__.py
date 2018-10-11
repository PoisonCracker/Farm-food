from flask import Blueprint

home = Blueprint('home', __name__)

import APP.home.view
