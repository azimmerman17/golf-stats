from app.extensions import get_country_subdivision, run_query, db_connect, db_close
from app.models.facility import Facility
from app.models.facility_season import Facility_Season
from app.course.functions import upload_course

# load data from ghin and payload to the DB
def upload_facility(ghin_data=None, payload=None, method='POST'):
  # derive US state and validate 
  (state, country) = get_country_subdivision(ghin_data['CourseState']) if '-' in ghin_data['CourseState'] else (None, None)
  # create payload for the Facilty Table

  # set missing keys to None
  input_keys = ['classification', 'established', 'handle', 'website']
  for k in input_keys:
    payload[k] = None if k not in payload.keys() else payload[k]

  facility = {
    'facility_id': ghin_data['Facility']['FacilityId'],                 # GHIN
    'stack_facility_id': None,                                          # Stack File (needs solutioned)
    'name': ghin_data['Facility']['FacilityName'],                      # GHIN
    'classification': payload['classification'],                        # Manual
    'established': payload['established'],                              # Manual
    'handle': payload['handle'],                                        # Manual
    'website': payload['website'],                                      # Manual
    'address': ghin_data['Facility']['GeoLocationFormattedAddress'],    # GHIN
    'city': ghin_data['CourseCity'],                                    # Stack file then GHIN
    'state': state,                                                     # Stack file then GHIN
    'country': country,                                                 # Stack file then GHIN
    'geo_lat': ghin_data['Facility']['GeoLocationLongitude'],           # GHIN
    'geo_lon': ghin_data['Facility']['GeoLocationLatitude'],            # GHIN
  }
  season = {
    'facility_id': ghin_data['Facility']['FacilityId'],     # GHIN
    'start_date': ghin_data['Season']['SeasonStartDate'],   # GHIN
    'end_date': ghin_data['Season']['SeasonEndDate'],       # GHIN
    'year_round': ghin_data['Season']['IsAllYear'],         # GHIN
  }

  # INSERT record to DB
  conn = db_connect()
  try:
    run_query(Facility().insert_query(facility), conn)
    run_query(Facility_Season().insert_query(season), conn) 
  except Exception as error:
    print('ERROR: ', error)
    db_close(conn, action='rollback')
    return ({'msg': 'Error updating facility , cannont create course', 'status_code': 500}, 1)

  (msg, flag) = upload_course(ghin_data=ghin_data, payload=payload, method=method, conn=conn)

  if flag == 0:
    db_close(conn, action='commit')
    return msg
  else:
    db_close(conn, action='rollback')
    return msg

