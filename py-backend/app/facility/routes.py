from flask import request
from markupsafe import escape

from app.extensions import Engine
from app.facility import bp
from app.facility.functions import translate_ghin_data
from app.facility.queries import check_unique_facility, get_facility
from app.functions.sql_functions import run_query, open_conn, check_conn

from app.models.facility import Facility
from app.models.facility_season import Facility_Season

Facility_Season
from config import Config

# GET ALL FACILITIES, CREATE NEW FACILITY
@bp.route('/', methods=['GET', 'POST'])
def facility(config_class=Config):
  # GET ALL FACILITIES
  if request.method == 'GET':
    # get all the facilities query
    all_query = get_facility()
    
    try:
      res = run_query(all_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving facility list'}, 500

    return [Facility(f['facility_id'], f['name'], classification=f['classification'], hole_count=f['hole_count'], established=f['established'], handle=f['handle'], website=f['website'], address=f['address'], city=f['city'], state=f['state'], country=f['country'], geo_lat=f['geo_lat'], geo_lon=f['geo_lon']).as_dict() for f in res]
  # CREATE NEW FACILITY
  elif request.method == 'POST':
    # check if payload is valid
    if request.is_json == False:
      return {'msg': 'No JSON data to create new facility'}, 400
    # check if required fields are present
    elif any(item not in request.json.keys() for item in ['name', 'city', 'state', 'country']):
      return {'msg': 'Required field(s) missing for facility insert'}, 400
    
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
    # insert_query = Facility(None,name=data['name'], classification=data['classification'], hole_count=data['hole_count'], established=data['established'], handle=data['handle'], website=data['website'], address=data['address'], city=data['city'], state=data['state'], country=data['country'], geo_lat=data['geo_lat'], geo_lon=data['geo_lon']).insert_row(request.json)
    insert_query = Facility(None).insert_row(request.json)
    
    # open db connection
    conn = open_conn()

    # run insert query
    try:
      run_query(insert_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error inserting facility record'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Facility record instered successfully'}, 200
    else:
      return {'msg': 'Error inserting facility record'}, 500
  else:
    return {'msg': 'Method not allowed'}, 405

# GET ALL FROM A FACILITY BY ID, CREATE NEW COURSE, UPDATE & DELETE EXISTING FACILITY
@bp.route('/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def facility_id(id, config_class=Config):
  # GET FACILITY BY ID
  if request.method == 'GET':
    # get facilities query
    query = get_facility(escape(id))
    
    try:
      res = run_query(query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving facility'}, 500
    
    if len(res) != 1:
      return {'msg': 'Error: could not retrieve the requested facility'}, 500
    
    f = res[0]

    # Future work, build and return the entire facility
    return Facility(f['facility_id'], f['name'], classification=f['classification'], hole_count=f['hole_count'], established=f['established'], handle=f['handle'], website=f['website'], address=f['address'], city=f['city'], state=f['state'], country=f['country'], geo_lat=f['geo_lat'], geo_lon=f['geo_lon']).as_dict()
  # CREATE A NEW COURSE AT FACILITY
  elif request.method == 'POST':
    # check if payload is valid
    if request.is_json == False:
      return {'msg': 'No JSON data to create new course'}, 400

    # get current facility record
    query = get_facility(escape(id))

    try:
      res = run_query(query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Unable to confirm if facility exist'}, 500

    # check if there is a result, if there is data, do not insert new row
    if len(res) == 0:
      return {'msg': 'Facility not in database'}, 400

    f = res[0]

    # Transform facility cursor to dict
    f = {
      'facility': Facility(f['facility_id'], f['name'], classification=f['classification'], hole_count=f['hole_count'], established=f['established'], handle=f['handle'], website=f['website'], address=f['address'], city=f['city'], state=f['state'], country=f['country'], geo_lat=f['geo_lat'], geo_lon=f['geo_lon']).as_dict(),
      'season': Facility_Season(f['facility_season_id'] if 'facility_season_id' in f.keys() else None, facility_id=f['facility_id'], start_date=f['start_date'], end_date=f['end_date'], year_round=f['year_round']).as_dict()
    }

    # translate data from payload
    return translate_ghin_data(f, request.json, config_class)

    return {'msg': translate_ghin_data['msg']}, translate_ghin_data['status_code']

  # UPDATE FACILITY BY ID
  elif request.method == 'PUT':
    # get facility - validate facility exists
    check_query = get_facility(escape(id))

    try:
      res = run_query(check_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error updating facility'}, 500
    
    if len(res) != 1:
      return {'msg': 'Error: could not retrieve the requested facility'}, 500

    # update facility
    update_query = Facility(escape(id)).update_row(request.json)

    # open db connection
    conn = open_conn()

    # run update query
    try:
      run_query(update_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error updating facility record'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Facility record updated successfully'}, 200
    else:
      return {'msg': 'Error updating facility record'}, 500
  # DELETE FACILITY BY ID
  elif request.method == 'DELETE':
    # create delete query
    delete_query = Facility(escape(id)).delete_row()

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
      return {'msg': 'Error deleting facility record'}, 500
  else:
     return {'msg': 'Method not allowed'}, 405
