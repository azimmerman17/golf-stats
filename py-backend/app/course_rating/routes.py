from flask import request
from markupsafe import escape

from app.course_rating import bp
from app.course_rating.queries import get_course_rating
from app.functions.sql_functions import run_query, open_conn, check_conn
from app.models.course_rating import Course_Rating

from config import Config

# GET COURSE RATING BY ID, UPDATE EXISTING COURSE RATING 
@bp.route('/<int:id>', methods=['GET', 'PUT'])
def cours_rating_id(id, config_class=Config):
  if request.method == 'GET':
    # GET COURSE RATING 
    query = get_course_rating(escape(id))

    try:
      res = run_query(query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving course rating'}, 500
    
    if len(res) != 1:
      return {'msg': 'Error: could not retrieve the requested course rating'}, 500
    
    r = res[0]


    return Course_Rating(r['course_rating_id'], r['tee_id'], r['name'], r['hole_count'], r['gender'], r['start_hole'], r['course_rating'], r['slope'],  r['par'], r['bogey_rating'], r['effective_date']).as_dict()
  # UPDATING COURSE RATING 
  elif request.method == 'PUT':
    #  validate rating exists
    check_query = get_course_rating(escape(id))
    
    try:
      res = run_query(check_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving course rating'}, 500
    
    if len(res) != 1:
      return {'msg': 'Error: could not retrieve the requested course rating'}, 500
    
    # update course rating 
    update_query = Course_Rating(escape(id)).update_row(request.json)
    
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
      return {'msg': 'Course Rating record updated successfully'}, 200
    else:
      return {'msg': 'Error updating course rating record'}, 500
  else:
    return {'msg': 'Method not allowed'}, 405
