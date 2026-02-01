from flask import request
from markupsafe import escape

from app.extensions import Engine
from app.person import bp
from app.functions.sql_functions import run_query, open_conn, check_conn

from app.person.queries import get_person, check_user

from app.models.person import Person

from config import Config

# GET ALL USERS, CREATE NEW USER
@bp.route('/', methods=['GET', 'POST'])
def person(config_class=Config):
  # GET ALL PEOPLE
  if request.method == 'GET':
    # get all the user query
    all_query = get_person()

    try:
      res = run_query(all_query).mappings().all()

    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving person list'}, 500

    return [Person(person_id=p['person_id'], last_name=p['last_name'], first_name=p['first_name'], email=p['email'], dob=p['dob'], height=p['height'], weight=p['weight'], nation=p['nation'], home_facility=p['home_facility'], player_type=p['player_type'], gender=p['gender'], handedness=p['handedness'], units_distance=p['units_distance'], units_speed=p['units_speed'], units_temp=p['units_temp'], units_weight=p['units_weight'], units_alt=p['units_alt']).as_dict() for p in res]
  # CREATE NEW FACILITY
  elif request.method == 'POST':
    # check if payload is valid
    if request.is_json == False:
      return {'msg': 'No JSON data to create new person'}, 400
    # check if required fields are present
    elif any(item not in request.json.keys() for item in ['last_name', 'first_name', 'email', 'username']):
      return {'msg': 'Required field(s) missing for person insert'}, 400

    data = request.json

    # check for unique email and username
    check_query = check_user(email=data['email'], username=data['username'])
    
    # run check query
    try:
      res_check = run_query(check_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error inserting person record'}, 500

    if len(res_check) > 0:
      return {'msg': 'Error: user already exists'}, 400

    # insert person into table
    insert_query = Person(None).insert_row(request.json)
    
    # open db connection
    conn = open_conn()

    # run insert query
    try:
      run_query(insert_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error inserting person record'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Person record instered successfully'}, 200
    else:
      return {'msg': 'Error inserting person record'}, 500
  else:
    return {'msg': 'Method not allowed'}, 405
