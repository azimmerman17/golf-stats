from datetime import date

from app.extensions import db, orm

# Model Contains Profile Information for Facilities
class Facility(db.Model):
  facility_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  name = db.Column(db.String(100), nullable=False)
  classification = db.Column(db.Enum('D','P','R','M','S','O', name='facility_classification'), nullable=False, server_default='O')
  hole_count = db.Column(db.Integer, db.CheckConstraint('hole_count > 0', name='check_facility_hole_count'), nullable=False, server_default='1')
  established = db.Column(db.Integer, db.CheckConstraint('established > 1400', name='check_facility_established'))
  handle = db.Column(db.String(25), nullable=False, unique=True)
  website = db.Column(db.String(100))
  address = db.Column(db.String(100))
  city = db.Column(db.String(50))
  state = db.Column(db.String(3))
  country = db.Column(db.String(3))
  geo_lat = db.Column(db.FLOAT, db.CheckConstraint('geo_lat > -90 AND geo_lat < 90', name='check_facility_geo_lat'))
  geo_lon = db.Column(db.FLOAT, db.CheckConstraint('geo_lon > -180 AND geo_lon < 180', name='check_facility_geo_lon'))
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  @orm.validates('hole_count')
  def validate_course_count(self, key, value):
    if value != None: 
      if value <= 0:
        raise ValueError(f'Invalid Course Count - {value} - A facility must have a course')
    return value

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

  def __init__(self, facility_id, name=None, classification=None, hole_count=None, established=None, handle=None, website=None, address=None, city=None, state=None, country=None, geo_lat=None, geo_lon=None, created_at=None, updated_at=None):
    self.facility_id = facility_id
    self.name = name
    self.classification = classification
    self.hole_count = hole_count
    self.established = established
    self.handle = handle
    self.website = website
    self.address = address
    self.city = city
    self.state = state
    self.country = country
    self.geo_lat = geo_lat
    self.geo_lon = geo_lon
    self.created_at = created_at
    self.updated_at = updated_at

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
    INSERT INTO "Facility" ({keys})
    VALUES ({values})
    ;"""

    return query

  def update_row(self, update_dict):
    query = """
    UPDATE "Facility"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key} = '{update_dict[key]}'"
    
    query = f"""{query}
    WHERE facility_id = {self.facility_id}
    ;"""

    return  query

  def delete_row(self):
    query = f"""
    DELETE FROM "Facility" 
    WHERE  facility_id = {self.facility_id}
    ;"""

    return query




    