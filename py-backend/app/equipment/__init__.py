from flask import Blueprint

bp = Blueprint('equipment', __name__, url_prefix='/equipment')

from app.equipment import routes