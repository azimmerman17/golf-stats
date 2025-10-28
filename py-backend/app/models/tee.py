from app.extensions import db, orm
from app.models.course import Course

# Model Contains Information for Courses Tees
class Tee(db.Model):
  tee_id = db.Column(db.Integer, primary_key=True)
  course_id = db.Column(db.Integer, db.ForeignKey(Course.course_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  name = db.Column(db.String, nullable=False)
  yards = db.Column(db.Integer, db.CheckConstraint('YARDS > 0', name='tee_yards_min'), nullable=False, server_default='7200')
  meters = db.Column(db.Integer, db.CheckConstraint('METERS > 0', name='tee_meters_min'), nullable=False, server_default='6600')
  hole_count = db.Column(db.Integer, db.CheckConstraint('HOLE_COUNT >= 1 AND HOLE_COUNT <= 18', name='check_tee_hole_count'), nullable=False, server_default='18')
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  @orm.validates('hole_count')
  def validate_hole_count(self, key, value):
    if not 0 < value < 18:
      raise ValueError(f'Invalid Hole Count - {value} - Courses must have a hole count between 1 to 18')
    return value

  @orm.validates('yards')
  def validate_yardage(self, key, value):
    if value < 0:
      raise ValueError(f'Invalid Yardage - {value} - Course must have a positive length')
    return value

  @orm.validates('meters')
  def validate_yardage(self, key, value):
    if value < 0:
      raise ValueError(f'Invalid Yardage - {value} - Course must have a length')
    return value

  def __init__(self, tee_id, course_id=None, name=None, yards=None, meters=None, hole_count=None, created_at=None, updated_at=None):
    self.tee_id = tee_id
    self.course_id = course_id
    self.name = name
    self.yards = yards
    self.meters = meters
    self.hole_count = hole_count

  def as_dict(self):
    keys = ['created_at', 'updated_at']
    return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in keys}
