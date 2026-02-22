from datetime import date

from app.extensions import db, orm
from app.models.equipment import Equipment

# Model Contains Equipment Data for persons
class Equipment_Spec(db.Model):
  equipment_spec_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  equipment_id = db.Column(db.Integer, db.ForeignKey(Equipment.equipment_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  loft = db.Column(db.FLOAT)
  lie = db.Column(db.FLOAT)
  length = db.Column(db.FLOAT)
  wieght = db.Column(db.FLOAT)
  club_head = db.Column(db.String(50))
  head_weight = db.Column(db.FLOAT)
  offset = db.Column(db.FLOAT)
  bounce = db.Column(db.FLOAT)
  swing_weight = db.Column(db.String(2))
  shaft = db.Column(db.String(50))
  shaft_flex = db.Column(db.String(5))
  shaft_weight = db.Column(db.FLOAT)
  grip = db.Column(db.String(50))
  grip_core_dia = db.Column(db.FLOAT)
  grip_weight = db.Column(db.FLOAT)
  grip_size = db.Column(db.FLOAT)
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  def __init__(self, equipment_spec_id=None, equipment_id=None, loft=None, lie=None, length=None, wieght=None, club_head=None, head_weight=None, offset=None, bounce=None, swing_weight=None, shaft=None, shaft_flex=None, shaft_weight=None, grip=None, grip_core_dia=None, grip_weight=None, grip_size=None, created_at=None, updated_at=None):
    self.equipment_spec_id = equipment_spec_id
    self.equipment_id = equipment_id
    self.loft = loft
    self.lie = lie
    self.length = length
    self.wieght = wieght
    self.club_head = club_head
    self.head_weight = head_weight
    self.offset = offset
    self.bounce = bounce
    self.swing_weight = swing_weight
    self.shaft = shaft
    self.shaft_flex = shaft_flex
    self.shaft_weight = shaft_weight
    self.grip = grip
    self.grip_core_dia = grip_core_dia
    self.grip_weight = grip_weight
    self.grip_size = grip_size
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
    INSERT INTO "Equipment_Specs" ({keys})
    VALUES ({values})
    ;"""

    return query

  def update_row(self, update_dict):
    query = """
    UPDATE "Equipment_Specs"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key}='{update_dict[key]}'"
    
    query = f"""{query}
    WHERE {f"equipment_id = {self.equipment_id}" if self.equipment_id is not None else ""}
    ;"""

    return  query

  def delete_row(self):
    query = f"""
    DELETE FROM "Equipment_Specs" 
    WHERE {f"equipment_id = {self.equipment_id}" if self.equipment_id is not None else ""}
    ;"""

    return query

