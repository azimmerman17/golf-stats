from app.extensions import db, orm
from app.models.facility import Facility


class Facility_Season(db.Model):
  facility_season_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  facility_id = db.Column(db.Integer, db.ForeignKey(Facility.facility_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False, unique=True)
  start_date = db.Column(db.String(50))
  end_date = db.Column(db.String(50))
  year_round = db.Column(db.Boolean, nullable=False, server_default='0')
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  
  def __init__(self, facility_season_id, facility_id=None, start_date=None, end_date=None, year_round=None, created_at=None, updated_at=None):
    self.facility_season_id = facility_season_id
    self.facility_id = facility_id
    self.start_date = start_date
    self.end_date = end_date
    self.year_round = year_round    

  def as_dict(self):
    keys = ['created_at', 'updated_at']
    return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in keys}

  def insert_row(self, data):
    keys=''
    values=''

    for k in data.keys():
      print(f"'{k}' '{data[k]}'")
      keys = f'{keys}{'' if keys == '' else ', '}{k}'
      values =  f"{values}{'' if values == '' else ', '}{f"'{data[k]}'"}"

    query = f"""
    INSERT INTO "Facility_Season" ({keys})
    VALUES ({values})
    ;"""

    return query
  
  def update_row(self, update_dict):
    query = """
    UPDATE "Facility_Season"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key} = '{update_dict[key]}'"
    
    query = f"""{query}
    WHERE facility_id = {self.facility_id}
    ;"""

