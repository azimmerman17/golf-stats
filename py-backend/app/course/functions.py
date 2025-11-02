from app.functions.sql_functions import run_query
from app.tee.queries import get_tee

from app.models.course import Course
from app.models.tee import Tee

# FUNCTION TO BUILD COURSE DICT
def build_course(courses):
  courses = [Course(c['course_id'], c['facility_id'], c['name'], c['hole_count'], c['established'], c['architect'], c['handle']).as_dict()for c in courses]

  # get tees for the courses 
  course_ids = [str(c1['course_id']) for c1 in courses]
  separator = ', '
  tee_query = get_tee(separator.join(course_ids), 'course_id')
  
  try:
    t_res = run_query(tee_query).mappings().all()
  except Exception as error:
    print('ERROR: ', error)
    return {'msg': 'Error retrieving Tees'}, 500
  
  return [{
    'course': Course(c['course_id'], c['facility_id'], c['name'], c['hole_count'], c['established'], c['architect'], c['handle']).as_dict(),
    'tee': [Tee(t['tee_id'], t['course_id'], t['name'], t['yards'], t['meters'], t['hole_count']).as_dict() for t in t_res if t['course_id'] == c['course_id']]
  } for c in courses]
  
