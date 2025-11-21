from flask import request
from markupsafe import escape

from app.hole import bp
from app.hole.queries import get_hole
from app.functions.sql_functions import run_query, open_conn, check_conn
from app.models.hole import Hole

from config import Config

# GET HOLE BY ID
@bp.route('/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hole_id(id, config_class=Config):
  # GET HOLE BY ID
  if request.method == 'GET':
    # get HOLE query
    query = get_hole(escape(id))
    
    try:
      res = run_query(query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving hole'}, 500
    
    if len(res) != 1:
      return {'msg': 'Error: could not retrieve the requested hole'}, 500
    
    h = res[0]

    return Hole(h['hole_id'], h['tee_id'], h['number'], h['gender'], h['yards'], h['meters'], h['par'], h['si'], h['effective_date']).as_dict()
  # UPDATING COURSE RATING 
  elif request.method == 'PUT':
    #  validate rating exists
    check_query = get_hole(escape(id))
    
    try:
      res = run_query(check_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving course rating'}, 500
    
    if len(res) != 1:
      return {'msg': 'Error: could not retrieve the requested course rating'}, 500
    
    # update course rating 
    update_query = Hole(escape(id)).update_row(request.json)
    
    # open db connection
    conn = open_conn()

    # run update query
    try:
      run_query(update_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error updating hole record'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Hole record updated successfully'}, 200
    else:
      return {'msg': 'Error updating hole record'}, 500
  else:
    return {'msg': 'Method not allowed'}, 405
