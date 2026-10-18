from flask import request
from markupsafe import escape

from app.extensions import run_query, call_api
from app.course import bp
from app.course.queries import get_course
from app.course.functions import build_course, update_course
from config import Config


# GET ALL FROM A COURSE BY ID, UPDATE & DELETE EXISTING COURSE
@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def course_id(id, config_class=Config):
  if request.method == 'GET':
    try:
      res = run_query(get_course(escape(id))).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Unable to to retieve facility'}, 500

    return  build_course(res[0], full=True)
  if request.method == 'PUT':
     # validate data and that the data is new
    if request.is_json == False:
      return {'msg': 'No JSON data to update course'}, 400

    # check if course_id is in the table
    try:
      res = run_query(get_course(escape(id))).mappings().all()
      if len(res) == 0:
        return {'msg': 'Course does not exist'}, 400 
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Unable to confirm if course exists'}, 500

    return update_course(request.json, escape(id))
  if request.method == 'DELETE':
    try:
      run_query(Course(course_id=escape(id)).delete_query())
      return {'msg': f'Course {escape(id)} deleted'}, 200 
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': f'Error deleting Course {escape(id)}'}, 500 


# REFRESH COURSE DATA THROUGH GHIN
# @bp.route('/ghin/<int:id>', methods=['PUT'])
# def facility_ghin(id, config_class=Config):
