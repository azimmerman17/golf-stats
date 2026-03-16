from flask import Blueprint

bp = Blueprint('handicap', __name__, url_prefix='/handicap')

from app.handicap import routes