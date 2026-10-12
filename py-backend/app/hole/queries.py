# QUERY TO FETCH HOLES 
def get_hole(id=None, key='hole_id'):
  return f"""SELECT * FROM `golf-stats`.Hole 
    {f'WHERE {key} = {id}' if id is not None else ''}
    ;"""
    

