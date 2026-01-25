import requests

from app.functions.sql_functions import run_query, open_conn, check_conn

from app.models.facility import Facility
from app.models.facility_season import Facility_Season
from app.models.course import Course
from app.models.tee import Tee
from app.models.hole import Hole
from app.models.course_rating import Course_Rating
from app.models.hole_geo import Hole_Geo

# function to add cours GPS data from API
def insert_geo_data(course_id, gps_data):
  # define varibles for the GPS data
  handle = gps_data['handle']
  par_list = gps_data['tee'][0]['par']
  tee_lat_list = gps_data['teelat']
  tee_lon_list = gps_data['teelng'] 
  dl_lat_list = gps_data['doglat'] 
  dl_lon_list = gps_data['doglng'] 
  dl2_lat_list = gps_data['catlat'] 
  dl2_lon_list = gps_data['catlng'] 
  green_front_lat_list = gps_data['frontlat'] 
  green_front_lon_list = gps_data['frontlng'] 
  green_back_lat_list = gps_data['backlat'] 
  green_back_lon_list = gps_data['backlng'] 
  zoom_list = gps_data['zoom'] 
  rotation_list = gps_data['rotation'] 
  green_depth_list = gps_data['greendepth'] 
  print(par_list)
  # print(range(par_list))

  # open db connection
  conn = open_conn()

  for i in range(18):
    if par_list[i] < 1:
      print('No new holes to add')
      break
    
    geo_dict = {
      'course_id': course_id,
      'number': i + 1,
      'handle': handle,
      'tee_lat': tee_lat_list[i],
      'tee_lon': tee_lon_list[i],
      'dl_lat': dl_lat_list[i] if dl_lat_list[i] != 0.0 else None,
      'dl_lon': dl_lon_list[i] if dl_lon_list[i] != 0.0 else None,
      'dl2_lat': dl2_lat_list[i] if dl2_lat_list[i] != 0.0 else None,
      'dl2_lon': dl2_lon_list[i] if dl2_lon_list[i] != 0.0 else None,
      'green_center_lat': (green_front_lat_list[i] + green_back_lat_list[i]) / 2,
      'green_center_lon': (green_front_lon_list[i] + green_back_lon_list[i]) / 2,
      'green_front_lat': green_front_lat_list[i],
      'green_front_lon': green_front_lon_list[i],
      'green_back_lat': green_back_lat_list[i],
      'green_back_lon': green_back_lon_list[i],
      'zoom': zoom_list[i],
      'rotation': rotation_list[i],
      'green_depth': green_depth_list[i],
    }

    geo_query = Hole_Geo(None).insert_row(geo_dict)

    # run update query
    try:
      run_query(geo_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error inserting course gps row data', 'status_code': 500}

    #  check connection - open = success, closed = fail
  if check_conn(conn) == True:
    conn.commit()
    conn.close()
    return {'msg':'Hole GPS and GHIN data instered successfully', 'status_code': 200}

# function to add hole data from ghin data
def translate_ratings(tee_id, pars, tee, conn):
  for rating in tee['Ratings']:
    # set the par value:
    if rating['RatingType'] == 'Front':
      par = pars['front']
    elif rating['RatingType'] == 'Front':
      par = pars['back']
    else:
      par = tee['TotalPar']

    rating_dict = {
      'tee_id': tee_id,
      'name': rating['RatingType'],
      'hole_count': tee['HolesNumber'] if rating['RatingType'] == 'Total' else 9,
      'gender': 'M' if tee['Gender'] == 'Male' else 'F',
      'start_hole': 10 if rating['RatingType'] == 'Back' else 1,
      'course_rating': rating['CourseRating'],
      'slope': round(rating['SlopeRating']),
      'par': par,
      'bogey_rating': rating['BogeyRating']
    }

    # build rating query
    rating_query = Course_Rating(None).insert_row(rating_dict)
    
    # run query
    try:
      run_query(rating_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error inserting rating row data', 'status_code': 500}

  return  {'msg': 'GHIN translation successfully completed', 'status_code': 200}

# function to add hole data from ghin data
def translate_holes(tee_id, action, user, tee, conn):
  # set pars varibles for the ratings
  par_front = 0
  par_back = 0

  # Add the holes to the DB
  for hole in tee['Holes']:
    if hole['Number'] <= 9:
      par_front += hole['Par']
    else:
      par_back += hole['Par']
       
    hole_dict = {
      # 'hole_id': hole['HoleId'],
      'tee_id': tee_id,
      'number': hole['Number'],
      'gender': 'M' if tee['Gender'] == 'Male' else 'F',
      'yards': hole['Length'],
      'meters': round(hole['Length'] * 0.9144),
      'par': hole['Par'],
      'si': hole['Allocation']
    }

    hole_query = Hole(None).insert_row(hole_dict)
  
    # run query
    try:
      run_query(hole_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error inserting hole row data', 'status_code': 500}

  return {'front': par_front, 'back': par_back}

# function to add tee data from ghin data
def translate_tees(user, ghin, conn):
  # list to store added tee names translated, prevents Male/Female duplicates
  translated_tees = {}

  for tee in ghin['TeeSets']:
    # check if tee was previously added
    if tee['TeeSetRatingName'] in translated_tees.keys():
      print(f'Tee {tee['TeeSetRatingName']} prevouisly insersted')
      tee_id = translated_tees[tee['TeeSetRatingName']]
      flag = 'update'
    else:
      print('Insery new tee')
      flag = 'insert'
      tee_dict = {
        'course_id':  ghin['CourseId'],
        'name': tee['TeeSetRatingName'],
        'yards': tee['TotalYardage'],
        'meters': tee['TotalMeters'],
        'hole_count': tee['HolesNumber']
      }
      # build tee query
      tee_query = Tee(None, yards=tee_dict['yards'], meters=tee_dict['meters'],hole_count=tee_dict['hole_count']).insert_row(tee_dict)
      # run query
      try:
        res = run_query(tee_query, conn).mappings().all()
        tee_id = res[0]['tee_id']
        translated_tees[tee_dict['name']] = res[0]['tee_id']
      except Exception as error:
        print('ERROR: ', error)
        return {'msg': 'Error inserting tee row data', 'status_code': 500}

    pars = translate_holes(tee_id, flag, user, tee, conn)
    if 'msg' in pars.keys():
      return pars

    msg = translate_ratings(tee_id, pars, tee, conn)
    if msg['status_code'] == 500:
      return msg

  return msg

# function to add course data from ghin data
def translate_course(facility_id, handle, user, ghin):
  # compile course information
  course_dict = {
    'course_id': ghin['CourseId'],
    'facility_id': facility_id,
    'name': ghin['CourseName'],
    'handle': handle,
    'established': user['established'],
    'architect': user['architect'],
    'hole_count': user['hole_count']
  }

  # build course query
  course_query = Course(None,hole_count=course_dict['hole_count'], established=course_dict['established']).insert_row(course_dict)
   
   # open db connection
  conn = open_conn()

  # run update query
  try:
    run_query(course_query, conn)
  except Exception as error:
    print('ERROR: ', error)
    return {'msg': 'Error inserting course row data', 'status_code': 500}

  msg = translate_tees(user, ghin, conn)

  #  check connection - open = success, closed = fail
  if check_conn(conn) == True:
    conn.commit()
    conn.close()

  return msg

# function the inserts/update facility data from ghin data
def translate_facility(facility_id, season_id, user, ghin):
  # update facility  record
  facility_dict = {
    'facility_id': ghin['Facility']['FacilityId'],
    'name': ghin['Facility']['FacilityName'],
  }

  # build facility query
  facility_query = Facility(facility_id).update_row(facility_dict)
  facility_id = ghin['Facility']['FacilityId']

  # check and update facility season record
  season_dict = {
    'facility_id': facility_id,
    'start_date': ghin['Season']['SeasonStartDate'],
    'end_date': ghin['Season']['SeasonEndDate'],
    'year_round': ghin['Season']['IsAllYear']
  }

  # check and update facility season record
  season_dict = {
    'facility_id': facility_id,
    'start_date': ghin['Season']['SeasonStartDate'],
    'end_date': ghin['Season']['SeasonEndDate'],
    'year_round': ghin['Season']['IsAllYear']
  }

  # build season query
  if season_id == None:
    season_query = Facility_Season(None).insert_row(season_dict)
  else:
    season_query = Facility_Season(season_id, facility_id).update_row(season_dict)

  # open db connection
  conn = open_conn()

  # run update query
  try:
    run_query(facility_query, conn)
    run_query(season_query, conn)
  except Exception as error:
    print('ERROR: ', error)
    return {'msg': 'Error updating facility , cannont create course', 'status_code': 500}

  # check connection - open = success, closed = fail
  if check_conn(conn) == True:
    conn.commit()
    conn.close()
    return facility_id
  else:
    return {'msg': 'Error updating facility records, cannont create course', 'status_code': 500}

# Function to create course from GHIN API data
def translate_ghin_data(facility, data, CONFIG):
  # separate the user entered and ghin passed in data
  User = data['User']
  GHIN = data['GHIN']

  season_id = facility['season']['facility_season_id']
  facility_id = translate_facility(facility['facility']['facility_id'], season_id, User, GHIN)

  if isinstance(facility_id, dict):
    return facility_id

  course_id  = GHIN['CourseId']
  handle = User['course_handle'] if User['course_handle'] != None else facility['facility']['handle']

  course_msg = translate_course(facility_id, handle, User, GHIN)

  if course_msg['status_code'] == 500:
    return course_msg
  
  print(course_msg['msg'])

  # course added, adding course data
  geo_msg = insert_geo_data(course_id, data['gps_data'])

  return  geo_msg

  
