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
  query = f"""
    SELECT F.* FROM "Facility" F
    {f'WHERE F.facility_id = {id}' if id is not None else ''}
    ;"""
    
  return query