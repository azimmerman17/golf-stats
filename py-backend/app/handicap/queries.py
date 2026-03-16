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

def get_current(id):
  query = f"""SELECT HH.* FROM "Handicap_History" HH
  WHERE HH.person_id = {id}
    AND HH.rev_date = (SELECT MAX(HH1.rev_date) FROM "Handicap_History" HH1
                      WHERE HH1.person_id = HH.person_id
                        AND HH1.rev_date <= NOW());"""

  return query
