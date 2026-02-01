from flask import Blueprint

bp = Blueprint('person', __name__, url_prefix='/person')

from app.person import routes

