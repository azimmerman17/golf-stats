from flask import Blueprint

bp = Blueprint('tee', __name__, url_prefix='/tee')

from app.tee import routes