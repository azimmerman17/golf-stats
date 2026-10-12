# QUERY TO FETCH TEES 
def get_tee(id=None, key='tee_id'):
  return f"""SELECT * FROM `golf-stats`.Tee 
    {f'WHERE {key} = {id}' if id is not None else ''}
    ;"""
    