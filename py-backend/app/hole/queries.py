#QUERY TO GET HOLE DATA
def get_hole(id, key='hole_id'):
  query = f"""SELECT H.* FROM "Hole" H
    WHERE H.{key} IN ({id})
    ;"""
    
  return query