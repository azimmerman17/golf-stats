from app.extensions import db, orm
from app.models.tee import Tee

# Model Contains Information for Courses Ratings
class Course_Rating(db.Model):
  __tablename__ = 'Course_Rating'
  course_rating_id = db.Column(db.Integer, primary_key=True)
  tee_id = db.Column(db.Integer, db.ForeignKey(Tee.tee_id, onupdate="CASCADE", ondelete="CASCADE"))
  name = db.Column(db.String(50), nullable=False)  # FRONT, BACK, FULL, ETC
  hole_count = db.Column(db.Integer, db.CheckConstraint('hole_count = 9 OR hole_count = 18', name='check_course_rating_hole_count'), server_default='18')
  gender = db.Column(db.Enum('M','F', name='course_rating_gender'), nullable=False, server_default='M')
  start_hole = db.Column(db.Integer, db.CheckConstraint('start_hole >= 1 AND start_hole <= 18', name='check_course_rating_start_hole'), nullable=False, server_default='1')
  course_rating = db.Column(db.FLOAT, nullable=False)
  slope = db.Column(db.Integer, db.CheckConstraint('slope >= 55 AND slope <= 155', name='check_course_rating_slope'), nullable=False)
  par = db.Column(db.Integer, db.CheckConstraint('par >= 27 AND par <= 80', name='check_course_rating_par'), nullable=False)
  bogey_rating = db.Column(db.FLOAT)
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  @orm.validates('hole_count')
  def validate_hole_count(self, key, value):
    if value is not None:
      if int(value) != 9 and int(value) != 18:
        raise ValueError(f'Invalid Hole Count - {value} - Invalid Hole Counts, Handicap hole counts must be 9 or 18')
      return value

  @orm.validates('start_hole')
  def validate_start_hole(self, key, value):
    if value is not None:
      if not 0 < value < 18:
        raise ValueError(f'Invalid Start Hole - {value} - Start Hole must be > 1 and <= 18')
      return value

  @orm.validates('slope')
  def validate_slope(self, key, value):
    if value is not None:
      if not 55 <= value <= 155:
        raise ValueError(f'Invalid Slope Value - {value} - Slope Value must be between 55 and 155')
      return value

  @orm.validates('par')
  def validate_slope(self, key, value):
    if value is not None:
      if not 27 <= value <= 80:
        raise ValueError(f'Invalid Par Value - {value} - PAr Value must be between 27 and 80')
      return value
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs) 