from flask import Blueprint

bp = Blueprint('seeder', __name__, url_prefix='/seeder')

from app.seeders import routes