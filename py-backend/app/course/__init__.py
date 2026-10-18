from flask import Blueprint

bp = Blueprint('course', __name__, url_prefix='/course')

from app.course import routes