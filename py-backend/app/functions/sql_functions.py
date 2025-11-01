from app.extensions import db, Engine

# FUNCTION TO OPEN A NEW DBCONNECTION
def open_conn():
  c = Engine.connect()
  c.begin()
  return c

# FUNCTION TO RUN A QUERY
def run_query(query, conn=None, hide=False):

  flag = 0
  # if connection not passed in, connect to db
  if conn == None:
    conn = open_conn()
    flag = 1

  # run the query
  try:
    result = conn.execute(db.text(query))
  except Exception as error:
    print('EXCEPTION - ', error)
    conn.rollback()
    conn.close()
    return error

  if hide == False:
    print('SQL QUERY:', query)

  # close connection if connection was created within function
  if flag == 1:
    conn.close()

  return result

# FUNCTION TO CHECK IF A CONNECTION REMAINS OPEN
def check_conn(c):
  try:
    c.info
  except Exception as error:
    print(error)
    return False
  
  return True