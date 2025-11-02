from flask import request
from markupsafe import escape

from app.extensions import Engine
from app.course import bp
from app.course.queries import get_course
from app.functions.sql_functions import run_query, open_conn, check_conn


from app.models.course import Course

from config import Config

# GET ALL COURSES OR CREATE A NEW COURSE REQUEST (LATER)
@bp.route('/', methods=['GET', 'POST'])
def course(config_class=Config):
  if request.method == 'GET':
    # get all the courses
    all_course_query = get_course()

    try:
      res = run_query(all_course_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving course list'}, 500

    return [Course(c['course_id'], c['facility_id'], c['name'], c['hole_count'], c['established'], c['architect'], c['handle']).as_dict() for c in res]
  else:
    return {'msg': 'Method not allowed'}, 405


# GET, UPDATE, OR DELETE COURSE BY ID, CREATE NEW TEE FOR COURSE
@bp.route('/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def course_id(id, config_class=Config):
  if request.method == 'GET':
    # get the course
    course_query = get_course(escape(id))

    try:
      res = run_query(course_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving course list'}, 500

    c = res[0]

    return Course(c['course_id'], c['facility_id'], c['name'], c['hole_count'], c['established'], c['architect'], c['handle']).as_dict()
  # UPDATE COURSE INFORMATION
  elif request.method == 'PUT':
    # get course - validate course exists
    check_query = get_course(escape(id))

    try:
      res = run_query(check_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error updating course'}, 500
    
    if len(res) != 1:
      return {'msg': 'Error: could not retrieve the requested course'}, 500

    # update facility
    update_query = Course(escape(id)).update_row(request.json)

    # open db connection
    conn = open_conn()

    # run update query
    try:
      run_query(update_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error updating course record'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Course record updated successfully'}, 200
    else:
      return {'msg': 'Error updating course record'}, 500
  elif request.method == 'DELETE':
    # create delete query
    delete_query = Course(escape(id)).delete_row(escape(id))

    # open db connection
    conn = open_conn()

    # run delete query
    try:
      run_query(delete_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error deleting facility record'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Facility record deleted successfully'}, 200

  else:
    return {'msg': 'Method not allowed'}, 405
