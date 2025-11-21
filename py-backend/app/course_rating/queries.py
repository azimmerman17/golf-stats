#QUERY TO GET COURSE RATING DATA
def get_course_rating(id, key='course_rating_id'):
  query = f"""SELECT CR.* FROM "Course_Rating" CR
    WHERE CR.{key} IN ({id})
    ;"""
    
  return query