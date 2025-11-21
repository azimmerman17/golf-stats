from flask import Blueprint

bp = Blueprint('course_rating', __name__, url_prefix='/course_rating')

from app.course_rating import routes