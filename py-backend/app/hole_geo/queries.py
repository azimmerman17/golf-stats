# QUERY TO GET HOLE GEO DATA
def get_hole_geo(id, key='hole_geo_id'):
  query = f"""SELECT HG.* FROM "Hole_Geo" HG
    WHERE HG.{key} IN ({id})
    ORDER BY HG.number asc
    ;"""
    
  return query