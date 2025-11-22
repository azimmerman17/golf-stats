from app.extensions import db, orm
from app.models.course import Course

# Model Contains Information for GPS Coordinated for each hole
class Hole_Geo(db.Model):
  hole_geo_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  course_id = db.Column(db.Integer, db.ForeignKey(Course.course_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  number = db.Column(db.Integer, db.CheckConstraint('number >= 1 AND number<= 18', name='check_hole_geo_number'), nullable=False)
  handle = db.Column(db.String(25), db.ForeignKey(Course.course_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  tee_lat = db.Column(db.FLOAT, db.CheckConstraint('tee_lat > -90 AND tee_lat < 90', name='check_hole_geo_tee_lat'))
  tee_lon = db.Column(db.FLOAT, db.CheckConstraint('tee_lon > -180 AND tee_lon < 180', name='check_hole_geo_tee_lon'))
  dl_lat = db.Column(db.FLOAT, db.CheckConstraint('dl_lat > -90 AND dl_lat < 90', name='check_hole_geo_dl_lat'))
  dl_lon = db.Column(db.FLOAT, db.CheckConstraint('dl_lon > -180 AND dl_lon < 180', name='check_hole_geo_dl_lon'))
  dl2_lat = db.Column(db.FLOAT, db.CheckConstraint('dl2_lat > -90 AND dl2_lat < 90', name='check_hole_geo_dl2_lat'))
  dl2_lon = db.Column(db.FLOAT, db.CheckConstraint('dl2_lon > -180 AND dl2_lon < 180', name='check_hole_geo_dl2_lon'))
  green_center_lat = db.Column(db.FLOAT, db.CheckConstraint('green_center_lat > -180 AND green_center_lat < 180', name='check_hole_geo_green_center_lat'))
  green_center_lon = db.Column(db.FLOAT, db.CheckConstraint('green_center_lon > -90 AND green_center_lon < 90', name='check_hole_geo_green_center_lon'))
  green_front_lat = db.Column(db.FLOAT, db.CheckConstraint('green_front_lat > -180 AND green_front_lat < 180', name='check_hole_geo_green_front_lat'))
  green_front_lon = db.Column(db.FLOAT, db.CheckConstraint('green_front_lon > -90 AND green_front_lon < 90', name='check_hole_geo_green_front_lon'))
  green_back_lat = db.Column(db.FLOAT, db.CheckConstraint('green_back_lat > -180 AND green_back_lat < 180', name='check_hole_geo_green_back_lat'))
  green_back_lon = db.Column(db.FLOAT, db.CheckConstraint('green_back_lon > -90 AND green_back_lon < 90', name='check_hole_geo_green_back_lon'))
  zoom = db.Column(db.Integer, db.CheckConstraint('zoom >= 1 AND zoom <= 20', name='check_hole_geo_zoom'))
  rotation = db.Column(db.FLOAT, db.CheckConstraint('rotation >= 0 AND rotation < 360', name='check_hole_geo_rotation'))
  green_depth = db.Column(db.FLOAT)
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  @orm.validates('number')
  def validate_number(self, key, value):
    if value is not None:
      if not 0 < value <= 18:
        raise ValueError(f'Invalid Hole Number - {value} - A hole number must be between 1 and 18')
      return value

  @orm.validates('zoom')
  def validate_zoom(self, key, value):
    if value is not None:
      if not 0 < value <= 18:
        raise ValueError(f'Invalid Zoom - {value} - Mapping API requires a zoom between 1 and 20')
      return value
  
  @orm.validates('rotation')
  def validate_zoom(self, key, value):
    if value is not None:
      if not 0 <= value < 360:
        raise ValueError(f'Invalid Rotation - {value} - Rotation value must me between 0 and 360')
      return value

  @orm.validates('tee_lat')
  @orm.validates('dl_lat')
  @orm.validates('dl2_lat')
  @orm.validates('green_center_lat')
  @orm.validates('green_front_lat')
  @orm.validates('green_back_lat')
  def validate_latatude(self, key, value):
    if value is not None:
      if not -90 < value < 90:
        raise ValueError(f'Invalid Latitude Value - {key}: {value} - The maximum and minimun latitude values on Earth is +/- 90 degrees, please check and resubmit your coordinates')
      return value

  @orm.validates('tee_lom')
  @orm.validates('dl_lom')
  @orm.validates('dl2_lom')
  @orm.validates('green_center_lom')
  @orm.validates('green_front_lom')
  @orm.validates('green_back_lom')
  def validate_lon(self, key, value):
    if value is not None:
      if not -180 < value < 180:
        raise ValueError(f'Invalid Longitude Value - {key}: {value} - The maximum and minimun longitude values on Earth is +/- 180 degrees, please check and resubmit your coordinates')
      return value

  def __init__(self, hole_geo_id, course_id=None, number=None, handle=None, tee_lat=None, tee_lon=None, dl_lat=None, dl_lon=None, dl2_lat=None, dl2_lon=None, green_center_lat=None, green_center_lon=None, green_front_lat=None, green_front_lon=None, green_back_lat=None, green_back_lon=None, zoom=None, rotation=None, green_depth=None, created_at=None, updated_at=None):
    self.hole_geo_id = hole_geo_id
    self.course_id = course_id
    self.number = number
    self.handle = handle
    self.tee_lat = tee_lat
    self.tee_lon = tee_lon
    self.dl_lat = dl_lat
    self.dl_lon = dl_lon
    self.dl2_lat = dl2_lat
    self.dl2_lon = dl2_lon
    self.green_center_lat = green_center_lat
    self.green_center_lon = green_center_lon
    self.green_front_lat = green_front_lat
    self.green_front_lon = green_front_lon
    self.green_back_lat = green_back_lat
    self.green_back_lon = green_back_lon
    self.zoom = zoom
    self.rotation = rotation
    self.green_depth = green_depth

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
    INSERT INTO "Hole_Geo" ({keys})
    VALUES ({values})
    ;"""

    return query
  
  def update_row(self, update_dict):
    query = """
    UPDATE "Hole_Geo"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key} = '{update_dict[key]}'"
    
    query = f"""{query}
    WHERE hole_geo_id = {self.facility_id}
    ;"""

    return query