# blueprint_module\__init__.py

from flask import Blueprint

blueprint = Blueprint('mblueprint', __name__)

from . import faceapp
# from . import app3