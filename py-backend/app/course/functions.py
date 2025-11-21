from app.functions.sql_functions import run_query
from app.tee.queries import get_tee
from app.hole.queries import get_hole
from app.course_rating.queries import get_course_rating

from app.models.course import Course
from app.models.tee import Tee
from app.models.hole import Hole
from app.models.course_rating import Course_Rating

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

  # get holes and ratings for the courses 
  tees = [Tee(t['tee_id'], t['course_id'], t['name'], t['yards'], t['meters'], t['hole_count']).as_dict() for t in t_res]
  
  hole_ids = [str(t1['tee_id']) for t1 in tees]
  separator = ', '
  hole_query = get_hole(separator.join(hole_ids), 'tee_id')
  rating_query = get_course_rating(separator.join(hole_ids), 'tee_id')


  try:
    h_res = run_query(hole_query).mappings().all()   
    r_res = run_query(rating_query).mappings().all()
  except Exception as error:
    print('ERROR: ', error)
    return {'msg': 'Error retrieving holes and ratings'}, 500

  for tee in tees:
    print(tee)
    tee['holes'] = {
      'M': [Hole(h['hole_id'], h['tee_id'], h['number'], h['gender'], h['yards'], h['meters'], h['par'], h['si'], h['effective_date']).as_dict() for h in h_res if h['tee_id'] == tee['tee_id'] and h['gender'] == 'M'],
      'F': [Hole(h['hole_id'], h['tee_id'], h['number'], h['gender'], h['yards'], h['meters'], h['par'], h['si'], h['effective_date']).as_dict() for h in h_res if h['tee_id'] == tee['tee_id'] and h['gender'] == 'F']
    }
    tee['course_rating'] = {
      'M': [Course_Rating(r['course_rating_id'], r['tee_id'], r['name'], r['hole_count'], r['gender'], r['start_hole'], r['course_rating'], r['slope'],  r['par'], r['bogey_rating'], r['effective_date']).as_dict() for r in r_res if r['tee_id'] == tee['tee_id'] and r['gender'] == 'M'],
      'F': [Course_Rating(r['course_rating_id'], r['tee_id'], r['name'], r['hole_count'], r['gender'], r['start_hole'], r['course_rating'], r['slope'],  r['par'], r['bogey_rating'], r['effective_date']).as_dict() for r in r_res if r['tee_id'] == tee['tee_id'] and r['gender'] == 'F']
    }

  return [{
    'course': Course(c['course_id'], c['facility_id'], c['name'], c['hole_count'], c['established'], c['architect'], c['handle']).as_dict(),
    'tees': [t for t in tees if t['course_id'] == c['course_id']]
  } for c in courses]
  
