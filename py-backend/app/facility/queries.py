# QUERY TO CHECK IF FACILITY IS UNIQUE
def check_unique_facility(data):
  query = f"""
    SELECT F.facility_id FROM "Facility" F
    WHERE F.name = '{data['name']}'
      AND F.city = '{data['city']}'
      AND F.state = '{data['state']}'
      AND F.country = '{data['country']}'
    ;"""

  return query

def get_facility(id=None):
  query = f"""SELECT F.*,
      S.facility_season_id,
      S.start_date,
      S.end_date,
      S.year_round 
    FROM "Facility" F
      LEFT JOIN "Facility_Season" S ON S.facility_id = F.facility_id
    {f'WHERE F.facility_id = {id}' if id is not None else ''}
    ORDER BY F.name
    ;"""
    
  return query
