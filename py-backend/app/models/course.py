from app.extensions import db, orm
from app.models.facility import Facility

# Model Contains Profile Information for Courses
# Facilities with multiple Courses should have Multiple Course Rows
class Course(db.Model):
  __tablename__ = 'Course'

  course_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  facility_id = db.Column(db.Integer, db.ForeignKey(Facility.facility_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  stack_course_id  = db.Column(db.String(50), unique=True)
  name = db.Column(db.String(50))
  hole_count = db.Column(db.Integer, db.CheckConstraint('hole_count >= 1 AND hole_count <= 18',  name='check_course_hole_count'), nullable=False, server_default='18')
  established = db.Column(db.Integer, db.CheckConstraint('established > 1400', name='check_course_established_min'))
  architect = db.Column(db.String(100))
  handle = db.Column(db.String(25), nullable=False, unique=True)
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  @orm.validates('hole_count')
  def validate_hole_count(self, key, value):
    if value is not None:
      if not 0 < value <= 18:
        raise ValueError(f'Invalid Hole Count - {value}')
      return value

  @orm.validates('established')
  def validate_established(self, key, value):
    if value is not None:
      if value < 1400:
        raise ValueError(f'Invalid Course Established Year - {value} - The first modern day course was esablished after 1400, please sumbit a later date.')
      elif value > date.today().year:
        raise ValueError(f'Invalid Course Established Year - {value} - Courses cannot have a future dated established year, it is likely this facility is still under construction, please resumbit this course once it opens.')
    return value

  def __init__(self, **kwargs):
    super().__init__(**kwargs) 