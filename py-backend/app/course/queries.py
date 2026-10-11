# QUERY TO FETCH COURSES 
def get_course(id=None, key='course_id'):
  return f"""SELECT C.* FROM `golf-stats`.Course C
    {f'WHERE C.{key} = {id}' if id is not None else ''}
    ;"""
    

