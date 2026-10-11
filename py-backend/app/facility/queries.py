# query to check if course exists in db
def check_unique_facility(data):
  return f"""
    SELECT 'Y' FROM `golf-stats`.Course
    WHERE course_id = {data['ghin_id']};"""