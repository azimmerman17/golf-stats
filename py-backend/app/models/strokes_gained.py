from datetime import date
from app.extensions import db, orm


# Model Contains Information for Strokes Gained Values
class Strokes_Gained(db.Model):
  strokes_gained_id = db.Column(db.Integer, primary_key=True)
  shot_code = db.Column(db.String(4), nullable=False, unique=True)
  distance = db.Column(db.Integer)
  lie = db.Column(db.Enum('T','F','R','B', 'S', 'X','P','H','G', name='Strokes_Gained_Lie'), nullable=False, server_default='T')
  pga_tour_value = db.Column(db.FLOAT, nullable=False)
  scratch_value = db.Column(db.FLOAT, nullable=False)
  per_shot_adjust = db.Column(db.FLOAT, nullable=False)
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  def __init__(self, strokes_gained_id=None, shot_code=None, distance=None, lie=None, pga_tour_value=None, scratch_value=None, per_shot_adjust=None, created_at=None, updated_at=None):
    self.strokes_gained_id = strokes_gained_id
    self.shot_code = shot_code
    self.distance = distance
    self.lie = lie
    self.pga_tour_value = pga_tour_value
    self.scratch_value = scratch_value
    self.per_shot_adjust = per_shot_adjust

  def as_dict(self):
    keys = ['created_at', 'updated_at']
    return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in keys}

  def insert_row(self, data):
    keys=''
    values=''

    for k in data.keys():
      keys = f'{keys}{'' if keys == '' else ', '}{k}'
      values =  f"{values}{'' if values == '' else ', '}{f"'{data[k]}'"}"

    query = f"""
    INSERT INTO "Strokes_Gained" ({keys})
    VALUES ({values})
    ON CONFLICT DO NOTHING
    ;"""

    return query

  def update_row(self, data):
    query = """
    UPDATE "Strokes_Gained"
    SET updated_at = NOW()"""

    for key in data.keys():
      query = f"{query}, {key}='{data[key]}'"
    
    query = f"""{query}
    WHERE strokes_gained_id = {self.strokes_gained_id}
    ;"""

    return query

  def seed_data(self, data):
    keys = 'shot_code, distance, lie, pga_tour_value, scratch_value, per_shot_adjust'
    values = ''  
    for d in data:
      if values != '':
        values = values + ',\n'
      values = values + f"('{d['shot_code']}', {d['distance']}, '{d['lie']}', {d['pga_tour_value']}, {d['scratch_value']}, {d['per_shot_adjust']})"
        
    query = f"""
    INSERT INTO "Strokes_Gained" ({keys})
	  VALUES {values}
    ON CONFLICT DO NOTHING
    ;"""

    return query
