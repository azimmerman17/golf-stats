from app.extensions import db, orm
from app.models.course import Course

# Model Contains Information for Courses Tees
class Tee(db.Model):
  __tablename__ = 'Tee'
  tee_id = db.Column(db.Integer, primary_key=True)
  course_id = db.Column(db.Integer, db.ForeignKey(Course.course_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  stack_tee_id = db.Column(db.String(25), unique=True)
  name = db.Column(db.String(50), nullable=False)
  color = db.Column(db.String(7))
  yards = db.Column(db.Integer, db.CheckConstraint('yards > 0', name='check_tee_yards'), nullable=False, server_default='7200')
  meters = db.Column(db.Integer, db.CheckConstraint('meters > 0', name='check_tee_meters'), nullable=False, server_default='6600')
  hole_count = db.Column(db.Integer, db.CheckConstraint('hole_count >= 1 AND hole_count <= 18', name='check_tee_hole_count'), nullable=False, server_default='18')
  # gender = db.Column(db.Enum('M','F', name='tee_rating_gender'), nullable=False, server_default='M')
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  @orm.validates('hole_count')
  def validate_hole_count(self, key, value):
    if value is not None:
      if not 0 < value <= 18:
        raise ValueError(f'Invalid Hole Count - {value} - Courses must have a hole count between 1 to 18')
      return value

  @orm.validates('yards')
  def validate_yardage(self, key, value):
    if value is not None:
      if value < 0:
        raise ValueError(f'Invalid Yardage - {value} - Course must have a positive length')
      return value

  @orm.validates('meters')
  def validate_yardage(self, key, value):
    if value is not None:
      if value < 0:
        raise ValueError(f'Invalid Yardage - {value} - Course must have a length')
      return value

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
    
    return f"""INSERT INTO `golf-stats`.`Tee` ({', '.join(cols)})
    VALUES ({', '.join(values)});"""