from app.extensions import db, orm
from app.models.facility import Facility

# Model to define the length of a posting season for a facility
class Facility_Season(db.Model):
  __tablename__ = 'Facility_Season'
  
  facility_season_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  facility_id = db.Column(db.Integer, db.ForeignKey(Facility.facility_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False, unique=True)
  start_date = db.Column(db.String(50))
  end_date = db.Column(db.String(50))
  year_round = db.Column(db.Boolean, nullable=False, server_default='0')
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  def __init__(self, **kwargs):
    super().__init__(**kwargs) 
  
  # Tramform to dict
  def as_dict(self):
    keys = ['created_at', 'updated_at']
    return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in keys}

  # INSERT record into the DB
  def insert_query(self, data):
    cols = []
    values =[]
    for k in data.keys():
      if data[k] is not None:
        quote = "'" if isinstance(data[k], str) == True else ""
        cols.append(k)
        values.append(f'{quote}{data[k]}{quote}')
    
    return f"""INSERT INTO `golf-stats`.`Facility_Season` ({', '.join(cols)})
    VALUES ({', '.join(values)});"""

# UPDATE record into the DB
  def update_query(self, data):
    print(data)
    values = ['updated_at = NOW()']
    for k in data.keys():
      quote = "'" if isinstance(data[k], str) == True else ""
      values.append(f'{k} = {quote}{data[k] if data[k] is not None else 'null'}{quote}')

    return f"""UPDATE `golf-stats`.`Facility_Season`
      SET {', '.join(values)}
      WHERE facility_id = {self.facility_id};"""
