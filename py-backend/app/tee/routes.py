from flask import request
from markupsafe import escape

from app.extensions import Engine
from app.tee import bp
from app.tee.queries import get_tee
from app.functions.sql_functions import run_query, open_conn, check_conn

from app.models.tee import Tee

from config import Config

# GET OR UPDATE A TEE, CREATE A NEW RATING
@bp.route('/<int:id>', methods=['GET', 'POST', 'PUT'])
def tee(id, config_class=Config):
  if request.method == 'GET':
    # get all the courses
    tee_query = get_tee(escape(id))

    try:
      res = run_query(tee_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving tee list'}, 500

    t = res[0]
    
    return Tee(t['tee_id'], t['course_id'], t['name'], t['yards'], t['meters'], t['hole_count']).as_dict()
  else:
    return {'msg': 'Method not allowed'}, 405

