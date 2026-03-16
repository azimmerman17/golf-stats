# Get GHIN Number for user
def get_ghin(id):
  query = f"""SELECT ghin_number FROM "Person"
  WHERE person_id = {id};"""

  return query

def get_history(id):
  query = f"""SELECT * FROM "Handicap_History"
  WHERE person_id = {id}
  ORDER BY rev_date DESC;"""

  return query
