# query to check if course exists in db
def check_unique_facility(data):
  return f"""
    SELECT 'Y' FROM `golf-stats`.Course
    WHERE course_id = {data['ghin_id']}
      And facility_id NOT IN (SELECT facility_id FROM `golf-stats`.Facility);"""

# query to get facility data
def get_facility(id=None):
  return f"""
    SELECT * FROM `golf-stats`.Facility
    {f'WHERE facility_id = {id}' if id is not None else ''};"""
  
# query to get facility season data
def get_facility_season(id):
  return f"""
    SELECT * FROM `golf-stats`.Facility_Season
    WHERE facility_id = {id};"""