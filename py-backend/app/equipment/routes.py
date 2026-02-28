from flask import request
from markupsafe import escape

from app.extensions import Engine
from app.equipment import bp
# from app.equipment.functions import translate_ghin_data
from app.equipment.queries import get_equipment, check_user
from app.equipment.functions import build_equipment_record
from app.functions.sql_functions import run_query, open_conn, check_conn

from app.models.equipment import Equipment
from app.models.equipment_spec import Equipment_Spec
from app.models.equipment_distance import Equipment_Distance

from config import Config

# GET ALL, update OR DELETE EQUIPMENT BY EQUIPMENT ID
@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def equipment_Id(id, config_class=Config):
  if request.method == 'GET':
    # GET EQUIPMENT QUERY
    (equip_query, equip_spec_query, equip_dist_query) = get_equipment(escape(id), 'equipment')
    
    # run querys
    try:
      equipment = run_query(equip_query).mappings().all()
      specs = run_query(equip_spec_query).mappings().all()
      distance = run_query(equip_dist_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retieving equipment records'}, 500

    # match records in 1 dict
    return build_equipment_record(equipment, specs, distance)
  elif request.method == 'PUT':
    # check if payload is valid
    if request.is_json == False:
      return {'msg': 'No JSON data to update equipment'}, 400

    # check if equipment exists
    check_query = get_equipment(id, 'check')

    # run check query
    try:
      res_check = run_query(check_query).mappings().all()
      if len(res_check) != 1:
        return {'msg': 'Error: validating equipment'}, 400
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error locating equipment record'}, 500

    # build queries for update
    club_query = Equipment(equipment_id=id).update_row(request.json['club']) if 'club' in request.json.keys() else None
    spec_query = Equipment_Spec(equipment_id=id).update_row(request.json['spec']) if 'spec' in request.json.keys() else None
    distance_query = Equipment_Distance(equipment_id=id).update_row(request.json['distance']) if 'distance' in request.json.keys() else None

    # open db connection
    conn = open_conn()

    try:
      # run delete queries
      if club_query is not None:
        run_query(club_query, conn)
      if spec_query is not None:
        run_query(spec_query, conn)
      if distance_query is not None:
        run_query(distance_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error updating equipment records'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Equipment records updated successfully'}, 200
    else:
      return {'msg': 'Error updating equipment records'}, 500
  elif request.method == 'DELETE':
    # build queries for delete
    club_query = Equipment(equipment_id=id).delete_row()
    spec_query = Equipment_Spec(equipment_id=id).delete_row()
    distance_query = Equipment_Distance(equipment_id=id).delete_row()

    # open db connection
    conn = open_conn()

    try:
      # run delete queries
      run_query(club_query, conn)
      run_query(spec_query, conn)
      run_query(distance_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error deleting equipment records'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Equipment records deleted successfully'}, 200
    else:
      return {'msg': 'Error deleting equipment records'}, 500
  else:
    return {'msg': 'Method not allowed'}, 405



# GET ALL, CREATE NEW, OR DELETE EQUIPMENT FOR A SINGLE PERSON
@bp.route('/user/<int:id>', methods=['GET', 'POST', 'DELETE'])
def equipment_user(id, config_class=Config):
    # GET EQUIPMENT BY USER ID
  if request.method == 'GET':
    # GET EQUIPMENT QUERY
    (equip_query, equip_spec_query, equip_dist_query) = get_equipment(escape(id), 'user')
    
    # run querys
    try:
      equipment = run_query(equip_query).mappings().all()
      specs = run_query(equip_spec_query).mappings().all()
      distance = run_query(equip_dist_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retieving equipment records'}, 500

    # match records in 1 dict
    return build_equipment_record(equipment, specs, distance)
  elif request.method == 'POST':
    # check if payload is valid
    if request.is_json == False:
      return {'msg': 'No JSON data to create new equipment'}, 400

    # check if person exists
    check_query = check_user(id)
    
    # run check query
    try:
      res_check = run_query(check_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error validating user'}, 500

    # if no person quit
    if len(res_check) != 1:
      return {'msg': 'Error: user does not exists'}, 400

    # open db connection
    conn = open_conn()

    try:
      # loop through payload to populate tables
      for n in request.json:
        
        # start with club
        club_query = Equipment(person_id=id).insert_row(n['club'])
        # run club query
        e_id = run_query(club_query, conn).mappings().first()['equipment_id']

        # build spec and distance queries
        spec_query = Equipment_Spec(equipment_id=e_id).insert_row(n['spec'])
        distance_query = Equipment_Distance(equipment_id=e_id).insert_row(n['distance'])
        # run insert queries
        run_query(spec_query, conn)
        run_query(distance_query, conn)

    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error inserting equipment records'}, 500

        # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Equipment records instered successfully'}, 200
    else:
      return {'msg': 'Error inserting equipment records'}, 500
  elif request.method == 'DELETE':
    # build the delete queries
    equip_query =  Equipment(person_id=id).delete_row()
    equip_spec_query = Equipment_Spec().delete_row(id)
    equip_dist_query = Equipment_Distance().delete_row(id)
    
    # open db connection
    conn = open_conn()

    try:
      # run delete queries
      run_query(equip_query, conn)
      run_query(equip_spec_query, conn)
      run_query(equip_dist_query, conn)

    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error deleting equipment records'}, 500

        # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Equipment records deleted successfully'}, 200
    else:
      return {'msg': 'Error deleting equipment records'}, 500
  else:
    return {'msg': 'Method not allowed'}, 405
