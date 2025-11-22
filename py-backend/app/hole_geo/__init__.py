from flask import Blueprint

bp = Blueprint('hole_geo', __name__, url_prefix='/hole_geo')

from app.hole_geo import routes