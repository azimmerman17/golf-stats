from flask import request
from markupsafe import escape

from app.extensions import run_query, call_api
from app.facility import bp
from app.facility.queries import check_unique_facility, get_facility
from app.facility.functions import upload_facility, build_facility, update_facility
from app.course.functions import upload_course

from app.models.facility import Facility
from config import Config

# GET ALL FACILITIES, CREATE NEW FACILITY
@bp.route('/', methods=['GET', 'POST'])
def facility(config_class=Config):
  if request.method == 'GET':
    try:
      res = run_query(get_facility()).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Unable to to retieve facilities'}, 500

    return [buildFacility(r) for r in res]
  elif request.method == 'POST':
    # validate data and that the data is new
    if request.is_json == False:
      return {'msg': 'No JSON data to create new facility'}, 400
    # check if required fields are present
    elif any(item not in request.json.keys() for item in ['ghin_id']):
      return {'msg': 'Required field(s) missing for facility insert'}, 400
    # check if data is already in db
    else:
      try:
        res = run_query(check_unique_facility(request.json)).mappings().all()
        if len(res) > 0:
          return {'msg': 'Facility already exists, updates must occur through the facility\'s profile'}, 400 
      except Exception as error:
        print('ERROR: ', error)
        return {'msg': 'Unable to confirm if facility does not exist'}, 500
   
    # New course varified - GET data from GHIN
    ghin_url = f'{Config.GHIN_BASE_URL}{Config.GHIN_COURSE_ENDPOINT}?courseId={request.json['ghin_id']}&include_altered_tees=false'
    ghin_headers = {'Authorization': f'Bearer {Config.GHIN_TOKEN}'}
    ghin_data = call_api(ghin_url, headers=ghin_headers)
    
    if ghin_data.status_code >= 400:
       return {'msg': 'GHIN API call failed', 'error': ghin_data.text}, ghin_data.status_code
    # Populate Database with data
    return  upload_facility(ghin_data=ghin_data.json(), payload=request.json)
  else:
    return {'msg': 'Method not allowed'}, 405

# GET ALL FROM A FACILITY BY ID, CREATE NEW COURSE, UPDATE & DELETE EXISTING FACILITY
@bp.route('/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def facility_id(id, config_class=Config):
  if request.method == 'GET':
    try:
      res = run_query(get_facility(id)).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Unable to to retieve facility'}, 500

    return  buildFacility(res[0], full=True)
  elif request.method == 'POST':
    # validate data and that the data is new
    if request.is_json == False:
      return {'msg': 'No JSON data to create new facility'}, 400
    # check if required fields are present
    elif any(item not in request.json.keys() for item in ['ghin_id']):
      return {'msg': 'Required field(s) missing for facility insert'}, 400
    # check if data is already in db
    else:
      try:
        res = run_query(check_unique_facility(request.json)).mappings().all()
        if len(res) != 0:
          return {'msg': 'Course already exists'}, 400 
        res = run_query(get_facility(id)).mappings().all()
        if len(res) == 0:
          return {'msg': 'Facility does not exist'}, 400 
      except Exception as error:
        print('ERROR: ', error)
        return {'msg': 'Unable to confirm if course/facility does (not) exist'}, 500

    # New course varified - GET data from GHIN
    ghin_url = f'{Config.GHIN_BASE_URL}{Config.GHIN_COURSE_ENDPOINT}?courseId={request.json['ghin_id']}&include_altered_tees=false'
    ghin_headers = {'Authorization': f'Bearer {Config.GHIN_TOKEN}'}
    ghin_data = call_api(ghin_url, headers=ghin_headers)
    
    if ghin_data.status_code >= 400:
      return {'msg': 'GHIN API call failed', 'error': ghin_data.text}, ghin_data.status_code
    # Populate Database with data
    return upload_course(ghin_data=ghin_data.json(), payload=request.json, method='POST')

      # return upload_course(ghin_data=request.json, payload=request.json, method='POST', conn=None)
  elif request.method == 'PUT':
    # validate data and that the data is new
    if request.is_json == False:
      return {'msg': 'No JSON data to update facility'}, 400

    # check if facility_id is in the table
    try:
      res = run_query(get_facility(id)).mappings().all()
      if len(res) == 0:
        return {'msg': 'Facility does not exist'}, 400 
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Unable to confirm if facility exists'}, 500

    return update_facility(request.json, id)
  elif request.method == 'DELETE':
    try:
      run_query(Facility(facility_id=id).delete_query())
      return {'msg': f'Facility {id} deleted'}, 200 
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': f'Error deleting Facility {id}'}, 500 
  else:
    return {'msg': 'Method not allowed'}, 405


