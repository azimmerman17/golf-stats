from flask import request
from markupsafe import escape

from app.extensions import Engine
from app.hole_geo import bp
from app.hole_geo.queries import get_hole_geo
from app.functions.sql_functions import run_query, open_conn, check_conn
from app.models.hole_geo import Hole_Geo

from config import Config

# GET OR UPDATE A HOLE GEO RECORD, CREATE A NEW RATING
@bp.route('/<int:id>', methods=['GET', 'PUT'])
def hole_geo(id, config_class=Config):
  # GET A SINGLE HOLE
  if request.method == 'GET':
    query = get_hole_geo(escape(id))

    try:
      res = run_query(query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving hole coordinates'}, 500
    
    if len(res) != 1:
      return {'msg': 'Error: could not retrieve the requested hole coordinates'}, 500
    
    r = res[0]
    return Hole_Geo(r['hole_geo_id'], r['course_id'], r['number'], r['handle'], r['tee_lat'], r['tee_lon'], r['dl_lat'], r['dl_lon'], r['dl2_lat'], r['dl2_lon'], r['green_center_lat'], r['green_center_lon'], r['green_front_lat'], r['green_front_lon'], r['green_back_lat'], r['green_back_lon'], r['zoom'], r['rotation'], r['green_depth']).as_dict()
  # UPDATE A SINGLE HOLE
  elif request.method == 'PUT':
    # validate rating exists
    check_query = get_hole_geo(escape(id))
    
    try:
      res = run_query(check_query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving hole geo record'}, 500
    
    if len(res) != 1:
      return {'msg': 'Error: could not retrieve the requested hole geo record'}, 500
    
    # update course rating 
    update_query = Hole_Geo(escape(id)).update_row(request.json)
    
    # open db connection
    conn = open_conn()

    # run update query
    try:
      run_query(update_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error updating hole geo record'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Hole Geo Record record updated successfully'}, 200
    else:
      return {'msg': 'Error updating Hole Geo Record '}, 500
  else:
    return {'msg': 'Method not allowed'}, 405
