from flask import Blueprint

bp = Blueprint('hole', __name__, url_prefix='/hole')

from app.hole import routes