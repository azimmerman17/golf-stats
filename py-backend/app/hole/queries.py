# QUERY TO FETCH HOLES 
def get_hole(id=None, key='hole_id'):
  return f"""SELECT * FROM `golf-stats`.Hole 
    {f'WHERE {key} = {id}' if id is not None else ''}
    ;"""
    
def get_hole_ghin(data):
  return f"""SELECT * FROM `golf-stats`.Hole
    WHERE tee_id = {data['tee_id']}
      AND number = {data['number']}
      AND gender = '{data['gender']}';"""

