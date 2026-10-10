from datetime import date

from app.extensions import db, orm

# Model Contains Profile Information for Facilities
class Facility(db.Model):
  __tablename__ = 'Facility'

  facility_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  stack_facility_id = db.Column(db.String(25),  unique=True)
  name = db.Column(db.String(100), nullable=False)
  classification = db.Column(db.Enum('D','P','R','M','S','O', name='facility_classification'), nullable=False, server_default='O')
  established = db.Column(db.Integer, db.CheckConstraint('established > 1400', name='check_facility_established'))
  handle = db.Column(db.String(25), nullable=False, unique=True)
  website = db.Column(db.String(100))
  address = db.Column(db.String(250))
  city = db.Column(db.String(50))
  state = db.Column(db.String(3))
  country = db.Column(db.String(3))
  geo_lat = db.Column(db.FLOAT, db.CheckConstraint('geo_lat > -90 AND geo_lat < 90', name='check_facility_geo_lat'))
  geo_lon = db.Column(db.FLOAT, db.CheckConstraint('geo_lon > -180 AND geo_lon < 180', name='check_facility_geo_lon'))
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  @orm.validates('established')
  def validate_established(self, key, value):
    if value != None: 
      if value < 1400:
        raise ValueError(f'Invalid Facility Established Year - {value} - The first writen record of golf is from 1457 and the first modern day course was esablished in 1574, please sumbit a later date.')
      elif value > date.today().year:
        raise ValueError(f'Invalid Facility Established Year - {value} - Facilities cannot have a future dated established year, it is likely this facility is still under construction, please resumbit this facility once it opens.')
    return value

  @orm.validates('geo_lat')
  def validate_geo_lat(self, key, value):
    if value != None: 
      if not -90 < value < 90:
        raise ValueError(f'Invalid Facility Latitude - {value} - The maximum and minimun latitude values on Earth is +/- 90 degrees, please check and resubmit your coordinates')
    return value

  @orm.validates('geo_lon')
  def validate_geo_lon(self, key, value):
    if value != None: 
      if not -180 < value < 180:
        raise ValueError(f'Invalid Facility Longitude - {value} - The maximum and minimun longitude values on Earth is +/- 180 degrees, please check and resubmit your coordinates')
    return value

  def __init__(self, **kwargs):
    super().__init__(**kwargs) 