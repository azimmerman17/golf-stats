# GET EQUIPMENT QUERIES
def get_equipment(id, schema=None):
  query = f"""
  Select * FROM "Equipment" E
  WHERE {'E.person_id' if schema == 'user' else 'E.equipment_id'} = {id}
  ORDER BY E.active desc,
    (CASE WHEN E.catagory = 'Driver' THEN 1
        WHEN E.catagory = 'Wood' THEN 2
        WHEN E.catagory = 'Hybrid' THEN 3
        WHEN E.catagory = 'Iron' THEN 4
        WHEN E.catagory = 'Wedge' THEN 5
        WHEN E.catagory = 'Putter' THEN 6
        ELSE 7
    END),
    (CASE 
      WHEN E.name LIKE 'P%' THEN '1'
      WHEN E.name LIKE 'G%' THEN '2'
      WHEN E.name LIKE 'S%' THEN '3'
      WHEN E.name LIKE 'L%' THEN '4'
      ELSE E.name
    END),
    E.year desc;
  """

  subquery = f"""
  Select E1.equipment_id FROM "Equipment" E1
  WHERE {'E1.person_id' if schema == 'user' else 'E1.equipment_id'} = {id}
  """

  spec_query = f"""
  Select ES.* FROM "Equipment_Spec" ES
  WHERE ES.equipment_id IN ({subquery});
  """

  dist_query = f"""
  Select ED.* FROM "Equipment_Distance" ED
  WHERE ED.equipment_id IN ({subquery});
  """
  if schema == 'check':
    return query
  return (query, spec_query, dist_query)

def check_user(id): 
  query = f"""
    SELECT P.person_id FROM "Person" P
    WHERE P.person_id = {id};
  """

  return query