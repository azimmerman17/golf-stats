from flask import request
from markupsafe import escape
from datetime import date, timedelta
import requests

from app.extensions import Engine
from app.handicap import bp
from app.functions.sql_functions import run_query, open_conn, check_conn
from app.handicap.queries import get_ghin, get_history, get_current
from app.handicap.functions import create_record

from app.models.handicap_history import Handicap_History

from config import Config

# GET ALL HANDICAP HISTORY RECORDS, CREATE NEW HISTORY RECORD FOR A USER
@bp.route('/<int:id>', methods=['GET', 'POST', 'DELETE'])
def handicap_history(id, config_class=Config):
  # GET HISTORY
  if request.method == 'GET':
    query = get_history(id)

    try:
      res = run_query(query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving person\'s history'}, 500

    return [Handicap_History(handicap_history_id=r['handicap_history_id'], person_id=r['person_id'], ghin_number=r['ghin_number'], assoc=r['assoc'], club=r['club'], hard_soft_cap=r['hard_soft_cap'], hard_cap=r['hard_cap'], soft_cap=r['soft_cap'], rev_date=r['rev_date'], hi_displsy=r['hi_displsy'], hi_value=r['hi_value'], low_hi_displsy=r['low_hi_displsy'], low_hi_value=r['low_hi_value']).as_dict() for r in res]
  # POST RECORD
  elif request.method == 'POST':
    # GET USER GHIN NUMBER
    ghin_query = get_ghin(id)

    try:
      res = run_query(ghin_query).mappings().all()
      if len(res) != 1:
        return {'msg': 'Error validating person\'s ghin'}, 500
      
      ghin = res[0]['ghin_number']
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving person\'s ghin'}, 500

    # Connect to GHIN
    GHIN_BASE = config_class.GHIN_BASE_URL

    # query parameters
    rev_count = 0
    date_end = date.today() + timedelta(days=1)
    date_begin = date.today() - timedelta(days=365)

    url = f'{GHIN_BASE}/golfers/{ghin}/handicap_history.json?rev_count={rev_count}&date_begin={date_begin}&date_end={date_end}'
    payload = {}
    headers = {
      # This token needs to be manually retrieved through logging into GHIN
      'Authorization': f'Bearer {config_class.GHIN_TOKEN}',
    }
    try:
      ghin_data = requests.request("GET", url, headers=headers, data=payload).json()
      if 'error' in ghin_data.keys():
        return {'msg': 'Invalid token for GHIN API, please log into GHIN a retreive a new token', 'ghin': ghin_data}, 500
      revisions = ghin_data['handicap_revisions']
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error connecting to the GHIN database, please log into GHIN a retreive a new token'}, 500

    # open db connection
    conn = open_conn()

    # LOOP GHIN RECORDS
    count = 0
    for record in revisions:
      rec = create_record(record, id)
      query = Handicap_History().insert_row(rec)
      
      try:
        run_query(query, conn)
        conn.commit()
        count += 1
      except Exception as error:
        print('ERROR: ', error)
        return {'msg': f'Error inserting Handicap History records - {count} records successfully inserted', 'count': count}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.close()
      return {'msg': f'Handicap History records inserted successfully - {count} records successfully inserted', 'count': count}, 200
    else:
      return {'msg': f'Error inserting Handicap History records - {count} records successfully inserted', 'count': count}, 500
  # DELETE ALL USER HISTORY
  elif request.method == 'DELETE':
    delete_query = Handicap_History().delete_row(id, 'person_id')
     
    # open db connection
    conn = open_conn()

    try:
      delete_query(query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': f'Error deleting Handicap History records'}, 500

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.close()
      return {'msg': f'Handicap History records deleted successfully'}, 200
    else:
      return {'msg': f'Error deleting Handicap History records'}, 500
  else:
    return {'msg': 'Method not allowed'}, 405

# GET CURRENT HANDICAP FOR A USER
@bp.route('/<int:id>/current', methods=['GET'])
def handicap_current(id, config_class=Config):
  # GET HISTORY
  if request.method == 'GET':
    query = get_current(id)
  
    try:
      res = run_query(query).mappings().all()
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error retrieving person\'s history'}, 500

    return [Handicap_History(handicap_history_id=r['handicap_history_id'], person_id=r['person_id'], ghin_number=r['ghin_number'], assoc=r['assoc'], club=r['club'], hard_soft_cap=r['hard_soft_cap'], hard_cap=r['hard_cap'], soft_cap=r['soft_cap'], rev_date=r['rev_date'], hi_displsy=r['hi_displsy'], hi_value=r['hi_value'], low_hi_displsy=r['low_hi_displsy'], low_hi_value=r['low_hi_value']).as_dict() for r in res][0]
  else:
    return {'msg': 'Method not allowed'}, 405
