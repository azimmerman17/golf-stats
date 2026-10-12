# QUERY TO FETCH COURSES 
def get_course_rating(id=None, key='course_rating_id'):
  return f"""SELECT * FROM `golf-stats`.Course_Rating 
    {f'WHERE {key} = {id}' if id is not None else ''}
    ;"""
    

