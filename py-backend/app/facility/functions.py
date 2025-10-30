from app.functions.sql_functions import run_query, open_conn, check_conn

from app.models.facility import Facility
from app.models.facility_season import Facility_Season


# build dicts to update facility records through GHIN load
def update_facility_ghin(db_data, ghin_data, keys):
  new_dict = {}
  for i in keys:
    cur_value = db_data[i]
  
  # set value from payload
    match i:
      case 'facility_id':
        target_value = ghin_data['Facility']['FacilityId']
      case 'name':
        target_value = ghin_data['Facility']['FacilityName']
      case 'start_date':
        target_value = ghin_data['Season']['SeasonStartDate']
      case 'end_date':
        target_value = ghin_data['Season']['SeasonEndDate']
      case 'year_round':
        target_value = ghin_data['Season']['IsAllYear']

    if cur_value != target_value:
      new_dict[i] = target_value
  
  return new_dict

# Function to create course from GHIN API data
def process_ghin_data(facility, data):
  #check and update facility record
  facility_dict = {
    'facility_id': data['Facility']['FacilityId'],
    'name': data['Facility']['FacilityName']
  }

  facility_id = data['Facility']['FacilityId']
  # check and update facility season record
    season_dict = {
      'facility_id': facility_id,
      'start_date': data['Season']['SeasonStartDate'],
      'end_date': data['Season']['SeasonEndDate'],
      'year_round': data['Season']['IsAllYear']
    }





    # open db connection
    conn = open_conn()

    # run update query
    try:
      run_query(update_facility_query, conn)
    except Exception as error:
      print('ERROR: ', error)
      return {'msg': 'Error updating facility , cannont create course'}

    # check connection - open = success, closed = fail
    if check_conn(conn) == True:
      conn.commit()
      conn.close()
    else:
      return {'msg': 'Error updating facility record, cannont create course'}
    
  facility_id = data['Facility']['FacilityId']
  # check and update facility season record
    season_dict = {
      'facility_id': facility_id,
      'start_date': data['Season']['SeasonStartDate'],
      'end_date': data['Season']['SeasonEndDate'],
      'year_round': data['Season']['IsAllYear']

  if facility['season']['facility_season'] == None
    }

    season_query = 
  else:
    update_season_dict = update_facility_ghin(facility['season'], data, ['start_date', 'end_date', 'year_round'])
    if len(update_season_dict.keys()) > 0:
      # generate update query
      season_query = Facility_Season(facility['facility_id']).update_row(update_facility_dict)





  # compile course information

  # set tees

    # set ratings for the tees
    # set holes for the tees

