from datetime import date

from app.extensions import db, orm
from app.models.equipment import Equipment

# Model Contains Equipment Distance Data
class Equipment_Distance(db.Model):
  equipment_distance_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  equipment_id = db.Column(db.Integer, db.ForeignKey(Equipment.equipment_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  manual_max_distance = db.Column(db.FLOAT)
  manual_stock_distance = db.Column(db.FLOAT)
  manual_knockdown_distance = db.Column(db.FLOAT)
  manual_shoulder_distance = db.Column(db.FLOAT)
  manual_hip_distance = db.Column(db.FLOAT)
  manual_knee_distance = db.Column(db.FLOAT)
  manual_dispersion = db.Column(db.FLOAT)
  calc_max_distance = db.Column(db.FLOAT)
  calc_stock_distance = db.Column(db.FLOAT)
  calc_knockdown_distance = db.Column(db.FLOAT)
  calc_shoulder_distance = db.Column(db.FLOAT)
  calc_hip_distance = db.Column(db.FLOAT)
  calc_knee_distance = db.Column(db.FLOAT)
  calc_dispersion = db.Column(db.FLOAT)
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  def __init__(self, equipment_distance_id=None, equipment_id=None, manual_max_distance=None, manual_stock_distance=None, manual_knockdown_distance=None, manual_shoulder_distance=None, manual_hip_distance=None, manual_knee_distance=None, manual_dispersion=None, calc_max_distance=None, calc_stock_distance=None, calc_knockdown_distance=None, calc_shoulder_distance=None, calc_hip_distance=None, calc_knee_distance=None, calc_dispersion=None, created_at=None, updated_at=None):
    self.equipment_distance_id = equipment_distance_id
    self.equipment_id = equipment_id
    self.manual_max_distance = manual_max_distance
    self.manual_stock_distance = manual_stock_distance
    self.manual_knockdown_distance = manual_knockdown_distance
    self.manual_shoulder_distance = manual_shoulder_distance
    self.manual_hip_distance = manual_hip_distance
    self.manual_knee_distance = manual_knee_distance
    self.manual_dispersion = manual_dispersion
    self.calc_max_distance = calc_max_distance
    self.calc_stock_distance = calc_stock_distance
    self.calc_knockdown_distance = calc_knockdown_distance
    self.calc_shoulder_distance = calc_shoulder_distance
    self.calc_hip_distance = calc_hip_distance
    self.calc_knee_distance = calc_knee_distance
    self.calc_dispersion = calc_dispersion
    self.created_at = created_at
    self.updated_at = updated_at

  def as_dict(self):
    keys = ['created_at', 'updated_at']
    return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in keys}

  def insert_row(self, data):
    keys=''
    values=''

    for k in data.keys():
      keys = f'{keys}{'' if keys == '' else ', '}{k}'
      values =  f"{values}{'' if values == '' else ', '}{f"'{data[k]}'" if data[k] is not None else 'null'}"

    query = f"""
    INSERT INTO "Equipment_Distance" ({keys})
    VALUES ({values})
    ;"""

    return query

  def update_row(self, update_dict):
    query = """
    UPDATE "Equipment_Distance"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key}='{update_dict[key]}'"
    
    query = f"""{query}
    WHERE {f"equipment_id = {self.equipment_id}" if self.equipment_id is not None else ""}
    ;"""

    return  query

  def delete_row(self):
    query = f"""
    DELETE FROM "Equipment_Distance" 
    WHERE {f"equipment_id = {self.equipment_id}" if self.equipment_id is not None else ""}
    ;"""

    return query
