# QUERY TO CHECK IF COURSE IS UNIQUE
def check_unique_course(data):
  query = f"""
    SELECT C.course_id FROM "Course" C
    WHERE (C.name = '{data['name']}'
      AND C.facility_id = '{data['facility_id']}')
      OR C.handle = '{data['handle']}'
    ;"""

  return query

# QUERY TO FETCH COURSES 
def get_course(id=None, key='course_id'):
  query = f"""SELECT C.* FROM "Course" C
    {f'WHERE C.{key} = {id}' if id is not None else ''}
    ;"""
    
  return query


