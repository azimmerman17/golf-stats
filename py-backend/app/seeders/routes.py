from flask import request
from markupsafe import escape

from app.seeders import bp
from app.functions.sql_functions import run_query, open_conn, check_conn
from app.models.strokes_gained import Strokes_Gained
from app.seeders.strokes_gained_seed import strokes_gained as sg_seed

from config import Config

# SEED STROKES GAINED TABLE
@bp.route('/strokes_gained', methods=['POST'])
def stroke_gained(config_class=Config):
  if request.method == 'POST':
    query = Strokes_Gained().seed_data(sg_seed)
    
    # open db connection
    conn = open_conn()
    
    try:
      run_query(query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error inserting sg data'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
      return {'msg': 'Strokes Gained records inserted successfully'}, 200
    else:
      return {'msg': 'Error inserting Strokes Gained records'}, 500
  else:
    return {'msg': 'Method not allowed'}, 405
    return query
