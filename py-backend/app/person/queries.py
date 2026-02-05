# query to retrieve user data 
def get_person(id=None, username=None):
  query = f"""SELECT P.* FROM "Person" P
    {f"""WHERE {f"P.person_id = {id}" if id is not None else ''}
      {f"P.username = '{username}'" if username is not None else ''}""" if id is not None or username is not None else ''};
  """

  return query

# query to see if username or email exists
def check_user(email=None, username=None):
  query = f"""SELECT P.* FROM "Person" P
    WHERE P.email = '{email}' 
      OR P.username = '{username}';
  """

  return query
