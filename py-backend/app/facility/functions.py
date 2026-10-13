from app.extensions import get_country_subdivision, get_country, us_state, run_query, db_connect, db_close
from app.models.facility import Facility
from app.models.facility_season import Facility_Season
from app.course.functions import upload_course, build_course
from app.course.queries import get_course
from app.facility.queries import get_facility_season

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
    'geo_lon': round(ghin_data['Facility']['GeoLocationLongitude'],5),  # GHIN
    'geo_lat': round(ghin_data['Facility']['GeoLocationLatitude'], 5),  # GHIN
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

# build a facility record
def build_facility(data, full=False):
  f = Facility(**data).as_dict()
  
  # get state and country data
  if f['country'] == 'USA' and f['state'] is not None:
    f['state'] = {
      'abbr': f['state'],
      'name': str(us_state(f['state']))
    }
    
  if f['country'] is not None:
    f['country'] = get_country(f['country'], 'alpha_3') if f['country'] is not None else f['country']

  # get courses that belong to the facilty
  try:
    courses = run_query(get_course(id=f['facility_id'], key='facility_id')).mappings().all()
    season = run_query(get_facility_season(f['facility_id'])).mappings().all() 

    return {
      'facility': f,
      'courses': [build_course(c, full) for c in courses],
      'season': Facility_Season(**season[0]).as_dict()
      }
  except Exception as error:
    print('ERROR: ', error)
    return {'msg': f'Unable to to retieve facility_id {f['facility_id']}'}, 500

def update_facility(data, id):
  try:
    if 'season' in data.keys():
      run_query(Facility_Season(facility_id=id).update_query(data['season']))
    else:
      run_query(Facility(facility_id=id).update_query(data))
    return {'msg': f'Facility {'season'  if 'season' in data.keys() else ''} Updated'}, 200
  except Exception as error:
    print('ERROR: ', error)
    return {'msg': f'Unable to update facility {'season'  if 'season' in data.keys() else ''}'}, 500


