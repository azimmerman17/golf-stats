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
  elif request.method == 'PUT':
    # get facility - validate tee exists
    check_query = get_tee(escape(id))

    try:
      res = run_query(check_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error updating tee'}, 500
    
    if len(res) != 1:
      return {'msg': 'Error: could not retrieve the requested tee'}, 500

    # update facility
    update_query = Tee(escape(id)).update_row(request.json)

    # open db connection
    conn = open_conn()

    # run update query
    try:
      run_query(update_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error updating tee record'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Tee record updated successfully'}, 200
    else:
      return {'msg': 'Error updating tee record'}, 500
  else:
    return {'msg': 'Method not allowed'}, 405
