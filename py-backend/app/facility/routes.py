from flask import request
from markupsafe import escape

from app.facility import bp

from config import Config

# GET ALL FACILITIES
@bp.route('/', methods=['GET'])
def facility(config_class=Config):
  if request.method == 'GET':
    return 'Hello Facility'