from app.functions.sql_functions import run_query, open_conn, check_conn

from app.models.facility import Facility
from app.models.facility_season import Facility_Season
from app.models.course import Course
from app.models.tee import Tee
from app.models.hole import Hole


# Function to create course from GHIN API data
def process_ghin_data(facility, data):
  # separate the user entered and ghin passed in data
  User = data['User']
  GHIN = data['GHIN']

  # update facility  record
  facility_dict = {
    'facility_id': GHIN['Facility']['FacilityId'],
    'name': GHIN['Facility']['FacilityName']
  }

  # build facility query
  facility_query = Facility(facility['facility']['facility_id']).update_row(facility_dict)
  facility_id = GHIN['Facility']['FacilityId']

# check and update facility season record
  season_dict = {
    'facility_id': facility_id,
    'start_date': GHIN['Season']['SeasonStartDate'],
    'end_date': GHIN['Season']['SeasonEndDate'],
    'year_round': GHIN['Season']['IsAllYear']
  }

  # build season query
  if facility['season']['facility_season_id'] == None:
    season_query = Facility_Season(None).insert_row(season_dict)
  else:
    season_query = Facility_Season(facility['season']['facility_season_id'], facility_id).update_row(season_dict)

  # open db connection
  conn = open_conn()

  # run update query
  try:
    run_query(facility_query, conn)
    run_query(season_query, conn)
  except Exception as error:
    print('ERROR: ', error)
    return {'msg': 'Error updating facility , cannont create course'}

  # check connection - open = success, closed = fail
  if check_conn(conn) == True:
    conn.commit()
    conn.close()
  else:
    return {'msg': 'Error updating facility records, cannont create course'}
    
  # compile course information
  course_dict = {
    'course_id': GHIN['CourseId'],
    'facility_id': facility_id,
    'name': GHIN['CourseName'],
    'handle': User['course_handle'] if User['course_handle'] != None else facility['facility']['handle'],
    'established': User['established'],
    'architect': User['architect'],
    'hole_count': User['hole_count']
  }

  # build course query
  course_query = Course(None,hole_count=course_dict['hole_count'], established=course_dict['established']).insert_row(course_dict)
  course_id = course_dict['course_id']
    # open db connection
  conn = open_conn()

  # run update query
  try:
    run_query(course_query, conn)
  except Exception as error:
    print('ERROR: ', error)
    return {'msg': 'Error inserting course row data'}

  # Add Tees to the database
  course_tees = GHIN['TeeSets']
  # list to store added tee names processed, prevents Male/Female duplicates
  tee_list = []
  
  for tee in course_tees:
    print(tee_list)
    # check if tee has been processed
    tee_id = None
    flag = False
    for t in tee_list: 
      print(t)   
      if t['name'] == tee['TeeSetRatingName']:
        tee_id =  t['tee_id']
        flag = True
        print('Skippping tee already inserted')
        break        
      
    # if new tee - add tee - Else skip to holes and ratings
    if tee_id == None:
      tee_dict = {
        'course_id': course_id,
        'name': tee['TeeSetRatingName'] ,
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
      tee_list.append({'tee_id': tee_id, 'name': tee['TeeSetRatingName']})
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error inserting tee row data'}

    # Initalize par values for ratings
    par_front = 0
    par_back = 0

    # Add the holes to the DB
    for hole in tee['Holes']:
      if hole['Number'] <= 9:
        par_front += hole['Par']
      else:
        par_back += hole['Par']

      hole_dict = {
        'hole_id': hole['HoleId'],
        'tee_id': tee_id,
        'number': hole['Number'],
        'yards': hole['Length'],
        'meters': round(hole['Length'] * 0.9144)
      }

      if tee['Gender'] == "Male":
        hole_dict['par_male'] = hole['Par']
        hole_dict['si_male'] = hole['Allocation']
      else:
        hole_dict['par_female'] = hole['Par']
        hole_dict['si_female'] = hole['Allocation']

      # insert hole record
      if flag == False:
        hole_query = Hole(hole_dict['hole_id']).insert_row(hole_dict)
      else:
        hole_query = Hole(hole_dict['hole_id']).update_row(hole_dict)
  
      # run query
      try:
        run_query(hole_query, conn)
      except Exception as error:
        print('ERROR: ', error)
        return {'msg': 'Error inserting hole row data'}

  