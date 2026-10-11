from app.extensions import run_query, db_connect, db_close
from app.models.tee import Tee
from app.course_rating.functions import upload_course_rating
from app.hole.functions import upload_hole

# fuction to upload data to Tee Table
def upload_tee(ghin_data=None, payload=None, method='POST', conn=None):
  if conn is None:
    conn = db_connect()

  # Loop through tees and add to DB
  tee_names = {}
  for tee in ghin_data['TeeSets']:
    if tee['TeeSetRatingName'] not in tee_names.keys():
      # add tee name to list to keep from duplicate addition
      tee_names[tee['TeeSetRatingName']] = tee['TeeSetRatingId']

      tee_data = {
        'tee_id': tee['TeeSetRatingId'],                      # GHIN
        'course_id': ghin_data['CourseId'],                   # GHIN
        'stack_tee_id': None,                                 # Stack
        'name': tee['TeeSetRatingName'],                      # GHIN
        'color': None,                                        # Stack
        'yards': tee['TotalYardage'],                         # GHIN
        'meters': tee['TotalMeters'],                         # GHIN
        'hole_count': payload['hole_count']                   # GHIN
      }

      try:
        run_query(Tee().insert_query(tee_data), conn)
      except Exception as error:
        print('ERROR: ', error)
        db_close(conn, action='rollback')
        return ({'msg': 'Error updating tee, cannont create course', 'status_code': 500}, 1)

      # add to the course ratings db
      (msg, flag) =  upload_course_rating(ghin_data=tee, payload=payload, method=method, conn=conn)
    
    if flag != 0:
      return (msg, flag)
    else: 
      tee['TeeSetRatingId'] = tee_names[tee['TeeSetRatingName']]

    # add to the course ratings db
    (msg, flag) =  upload_hole(ghin_data=tee, payload=payload, method=method, conn=conn)

    if flag != 0:
      return (msg, flag)

  return (msg, flag)
    

