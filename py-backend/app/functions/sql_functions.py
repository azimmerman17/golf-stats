# FUNCTION TO RUN A QUERY
def run_query(query, conn=None, hide=False):
  from app.extensions import db, Engine

  # if connection not passed in, connect to db
  if conn == None:
    conn = Engine.connect()
    conn.begin()
    flag = 1

  # run the query
  try:
    result = conn.execute(db.text(query))
  except Exception as error:
    print('Exception', error)
    conn.rollback()
    conn.close()
    return error

  if hide == False:
    print('SQL QUERY:', query)

  # close connection if connection was created within function
  if flag == 1:
    conn.close()

  return result