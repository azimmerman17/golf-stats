from flask import Blueprint

bp = Blueprint('facility', __name__, url_prefix='/facility')

from app.facility import routes