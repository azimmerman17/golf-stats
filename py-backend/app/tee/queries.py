#QUERY TO GET TEE DATA
def get_tee(id, key='tee_id'):
  query = f"""SELECT T.* FROM "Tee" T
    WHERE T.{key} IN ({id})
    ;"""
    
  return query