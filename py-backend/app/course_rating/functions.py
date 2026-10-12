from app.extensions import run_query, db_connect, db_close
from app.models.course_rating import Course_Rating

# fuction to upload data to Course Rating Table
def upload_course_rating(ghin_data=None, payload=None, method='POST', conn=None):
  if conn is None:
    conn = db_connect()

  # Loop through course ratings and add to DB
  for rating in ghin_data['Ratings']:
    #calculate par
    par = 0
    start_hole = 10 if rating['RatingType'] == 'Back' else 1
    count = 18 if rating['RatingType'] == 'Total' else 9

    for hole in ghin_data['Holes']:
      if hole['Number'] >= start_hole and count > 0:
        par += hole['Par']
        count -= 1

    rating_data = {
      'tee_id': ghin_data['TeeSetRatingId'],
      'name': rating['RatingType'],
      'hole_count': 18 if rating['RatingType'] == 'Total' else 9,
      'gender': ghin_data['Gender'][0],
      'start_hole': start_hole,
      'course_rating': rating['CourseRating'],
      'slope': rating['SlopeRating'],
      'par': par,
      'bogey_rating': rating['BogeyRating']
    }

    try:
      run_query(Course_Rating().insert_query(rating_data), conn)
    except Exception as error:
      print('ERROR: ', error)
      db_close(conn, action='rollback')
      return ({'msg': 'Error updating course ratings , cannont create course', 'status_code': 500}, 1)

  return ({'msg': 'Course Rating Created', 'status_code': 200}, 0)

def build_course_rating(rating):
  return Course_Rating(**rating).as_dict()