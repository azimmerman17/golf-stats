from flask import request
from markupsafe import escape

from app.facility import bp
from app.facility.queries import check_unique_facility
from app.functions.sql_functions import run_query

from app.models.facility import Facility

from config import Config

# GET ALL FACILITIES, CREATE NEW FACILITY
@bp.route('/', methods=['GET', 'POST'])
def facility(config_class=Config):
  if request.method == 'GET':
    return 'Hello Facility'
  elif request.method == 'POST':

    # check if payload is valid
    if request.is_json == False:
      return {'msg': 'No JSON data to create new facility'}, 400
    # check if required fields are present
    elif any(item not in request.json.keys() for item in ['name', 'city', 'state', 'country']):
      return {'msg': 'Required field(s) missing for facility insert'}, 400
    else:
      data = request.json

    # check if facility is new  -- Name, City, State, County combination must be unique
    check_unique_query = check_unique_facility(request.json)

    try:
      unique_res = run_query(check_unique_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Unable to confirm if facility does not exist'}, 500

    # check if there is a result, if there is data, do not insert new row
    if len(unique_res) > 0:
      return {'msg': 'Facility already exists'}, 200 

    # insert facility into table
    insert_query = Facility(None, data['name'], classification=data['classification'], hole_count=data['hole_count'], established=data['established'], handle=data['handle'], website=data['website'], address=data['address'], city=data['city'], state=data['state'], country=data['country'], geo_lat=data['geo_lat'], geo_lon=data['geo_lon']).insert_row()
    
    return insert_query

  else:
    return {'msg': 'Method not allowed'}, 405

# GET ALL FROM A FACILITY BY ID, CREATE NEW COURSE, UPDATE & DELETE EXISTING FACILITY
@bp.route('/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def facility_id(id, config_class=Config):
  if request.method == 'GET':
    return f'Hello Facility {escape(id)}'
  elif request.method == 'POST':
    print(request.json)
    return request.json
  else:
     return {'msg': 'Method not allowed'}, 405
