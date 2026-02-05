from datetime import date

from app.extensions import db, orm
from app.models.facility import Facility

# Model Contains Profile Information for People
class Person(db.Model):
  person_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  last_name = db.Column(db.String(25), nullable=False)
  first_name = db.Column(db.String(25), nullable=False)
  username = db.Column(db.String(25), nullable=False, unique=True)
  email = db.Column(db.String(50), nullable=False, unique=True)
  dob = db.Column(db.Date)
  height = db.Column(db.Float())
  weight = db.Column(db.Float())
  nation = db.Column(db.String(5))
  home_facility = db.Column(db.Integer, db.ForeignKey(Facility.facility_id, onupdate="CASCADE", ondelete="SET NULL"), nullable=False)
  player_type = db.Column(db.Enum('A', 'P', 'T', 'C', 'J', name='person_player_type'), nullable=False, server_default='A')
  gender =  db.Column(db.Enum('M', 'F', 'O', 'P', name='person_gender'), nullable=False, server_default='P')
  handedness = db.Column(db.Enum('L', 'R', name='person_handedness'), nullable=False, server_default='R')
  units_distance = db.Column(db.Enum('Y', 'M', name='person_units_distance'), nullable=False, server_default='Y')
  units_speed = db.Column(db.Enum('MPH', 'KPH', 'MPS', name='person_units_speed'), nullable=False, server_default='MPH')
  units_temp = db.Column(db.Enum('F', 'C', name='person_units_temp'), nullable=False, server_default='F')
  units_weight = db.Column(db.Enum('LB', 'KG', 'ST', name='person_units_weight'), nullable=False, server_default='LB')
  units_alt = db.Column(db.Enum('FT', 'M', name='person_units_alt'), nullable=False, server_default='FT')
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  def __init__(self, person_id=None, last_name=None, first_name=None, username=None, email=None, dob=None, height=None, weight=None, nation=None, home_facility=None, player_type=None, gender=None, handedness=None, units_distance=None, units_speed=None, units_temp=None, units_weight=None, units_alt=None, created_at=None, updated_at=None):
    self.person_id = person_id
    self.last_name = last_name
    self.first_name = first_name
    self.username = username
    self.email = email
    self.dob = dob
    self.height = height
    self.weight = weight
    self.nation = nation
    self.home_facility = home_facility
    self.player_type = player_type
    self.gender = gender
    self.handedness = handedness
    self.units_distance = units_distance
    self.units_speed = units_speed
    self.units_temp = units_temp
    self.units_weight = units_weight
    self.units_alt = units_alt
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
    INSERT INTO "Person" ({keys})
    VALUES ({values})
    ;"""

    return query

  def update_row(self, update_dict):
    query = """
    UPDATE "Person"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key}='{update_dict[key]}'"
    
    query = f"""{query}
    WHERE {f"person_id = {self.person_id}" if self.person_id is not None else ""}
          {f"username = '{self.username}'" if self.username is not None else ""}
    ;"""

    return  query

  def delete_row(self):
    query = f"""
    DELETE FROM "Person" 
    WHERE {f"person_id = {self.person_id}" if self.person_id is not None else ""}
          {f"username = '{self.username}'" if self.username is not None else ""}
    ;"""

    return query

