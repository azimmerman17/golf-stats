from datetime import date

from app.extensions import db, orm
from app.models.person import Person

# Model Contains Equipment Data for persons
class Equipment(db.Model):
  equipment_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  person_id = db.Column(db.Integer, db.ForeignKey(Person.person_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  catagory = db.Column(db.Enum('Driver', 'Wood', 'Hybrid', 'Iron', 'Wedge', 'Putter', name='equipment_type'), nullable=False)
  name = db.Column(db.String(25), nullable=False)
  short_name = db.Column(db.String(3), nullable=False)
  make = db.Column(db.String(25), nullable=False)
  model = db.Column(db.String(25), nullable=False)
  year =  db.Column(db.Integer)
  active = db.Column(db.Boolean, nullable=False, server_default='f')
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  def __init__(self, equipment_id=None, person_id=None, catagory=None, name=None, short_name=None, make=None, model=None, year=None, active=None, created_at=None, updated_at=None):
    self.equipment_id = equipment_id
    self.person_id = person_id
    self.catagory = catagory
    self.name = name
    self.short_name = short_name
    self.make = make
    self.model = model
    self.year = year
    self.active = active
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
    INSERT INTO "Equipment" ({keys})
    VALUES ({values})
    ;"""

    return query

  def update_row(self, update_dict):
    query = """
    UPDATE "Equipment"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key}='{update_dict[key]}'"
    
    query = f"""{query}
    WHERE {f"equipment_id = {self.equipment_id}" if self.equipment_id is not None else ""}
    ;"""

    return  query

  def delete_row(self):
    query = f"""
    DELETE FROM " b" 
    WHERE {f"equipment_id = {self.equipment_id}" if self.equipment_id is not None else ""}
    ;"""

    return query

