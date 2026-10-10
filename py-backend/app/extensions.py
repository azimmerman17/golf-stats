from flask_sqlalchemy import SQLAlchemy
import requests

from config import Config

# Initalize DB
db = SQLAlchemy()

#  Object Relational Mapper
orm = db.orm

# DB Engine
Engine = db.create_engine(
  Config.SQLALCHEMY_DATABASE_URI,
  pool_size=20,
  max_overflow=5
)

# connect to database
def db_connect():
  c = Engine.connect()
  c.begin()
  return c

def db_close(conn, action=None):
  if action == 'commit':
    conn.commit()
  elif action == 'rollback':
    conn.rollback()
  conn.close()

# run a query
def run_query(query, conn=None, hide=True):
  flag = 0
  if conn == None:
    conn = db_connect()
    flag = 1

  # run the query
  try:
    result = conn.execute(db.text(query))
  except Exception as error:
    print('Exception', error)
    db_close(conn, 'rollback')
    return error
  
  if hide == False:
    print('SQL QUERY:', query)

  if flag == 1:
    db_close(conn, 'commit')

  return result

# make api request
def call_api(url, methed='GET', payload={}, headers={}):
  return requests.request("GET", url, headers=headers, data=payload)
