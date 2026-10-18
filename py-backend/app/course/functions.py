from app.extensions import run_query, db_connect, db_close
from app.models.course import Course
from app.tee.functions import upload_tee, build_tee
from app.tee.queries import get_tee


# fuction to upload data to Course Table
def upload_course(ghin_data=None, payload=None, method='POST', conn=None):
  # set missing keys to None
  input_keys = ['hole_count', 'established', 'architect', 'handle']
  for k in input_keys:
    payload[k] = None if k not in payload.keys() else payload[k]

  course = {
    'course_id': ghin_data['CourseId'],                 # GHIN
    'facility_id': ghin_data['Facility']['FacilityId'], # GHIN 
    'stack_course_id': None,                            # Stack
    'name': ghin_data['CourseName'],                    # GHIN 
    'hole_count': payload['hole_count'],                # Manual
    'established': payload['established'],              # Manual
    'architect': payload['architect'],                  # Manual
    'handle': payload['handle'],                        # Manual
  }

  # INSERT record to DB
  c_flag = 1 if conn is None else 0
  if conn is None:
    conn = db_connect()
  try:
    run_query(Course().insert_query(course), conn)
  except Exception as error:
    print('ERROR: ', error)
    db_close(conn, action='rollback')
    flag = 1
    return ({'msg': 'Error updating course , cannont create course', 'status_code': 500}, 1)

  # Add Tees for the Course
  (msg, flag) = upload_tee(ghin_data=ghin_data, payload=payload, method=method, conn=conn)
  
  if c_flag == 1:
    if flag == 0:
      db_close(conn, action='commit')
      return msg
    else:
      db_close(conn, action='rollback')
      return msg 
  else:
    return (msg, flag)

# function to transform course model to dict
def build_course(course, full=True):
  course_dict = Course(**course).as_dict()
  # future development - continue to the Tee Dict
  if full == True:
    tees = run_query(get_tee(id=course_dict['course_id'], key='course_id')).mappings().all()
    course_dict['tees'] = [build_tee(t) for t in tees]
  
  return course_dict

def update_course(data, id):
  try:
    run_query(Course(course_id=id).update_query(data))
    return {'msg': 'Course Updated'}, 200
  except Exception as error:
    print('ERROR: ', error)
    return {'msg': 'Unable to update course'}, 500

