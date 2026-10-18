from app.extensions import run_query, db_connect, db_close
from app.hole.queries import get_hole_ghin
from app.models.hole import Hole

def upload_hole(ghin_data=None, payload=None, method='POST', conn=None):
  if conn is None:
    conn = db_connect()

  # Loop through tees and add to DB
  for hole in ghin_data['Holes']:
    hole_data = {
      'tee_id': ghin_data['TeeSetRatingId'],
      'number': hole['Number'],
      'gender': ghin_data['Gender'][0],
      'yards': hole['Length'],
      'meters': round(hole['Length'] * 0.9144),
      'par':hole['Par'],
      'si': hole['Allocation'],
    }

    try:
      if method == 'PUT':
        # get current hole
        current = run_query(get_hole_ghin(hole_data)).mappings().all()
        if len(current) > 0:
          run_query(Hole(**current[0]).update_ghin(hole_data), conn)
        else:
          run_query(Hole().insert_query(hole_data), conn)
      else:
        run_query(Hole().insert_query(hole_data), conn)
    except Exception as error:
      print('ERROR: ', error)
      db_close(conn, action='rollback')
      return ({'msg': 'Error updating hole, cannont create course', 'status_code': 500}, 1)

  return ({'msg': 'Course Created', 'status_code': 200}, 0)

def build_hole(hole):
  return Hole(**hole).as_dict()