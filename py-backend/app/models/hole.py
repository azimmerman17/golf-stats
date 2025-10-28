from app.extensions import db, orm
from app.models.tee import Tee

# Model Contains Information for each course hole
class Hole(db.Model):
  hole_id = db.Column(db.Integer, primary_key=True)
  tee_id = db.Column(db.Integer, db.ForeignKey(Tee.tee_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  number = db.Column(db.Integer, db.CheckConstraint('number >= 1 AND number <= 18', name='check_hole_number'), nullable=False)
  yards = db.Column(db.Integer, db.CheckConstraint('yards > 0 AND yards <= 999', name='check_hole_yards'), nullable=False, server_default='400')
  meters = db.Column(db.Integer, db.CheckConstraint('meters > 0 AND meters <= 999', name='check_hole_meters'), nullable=False, server_default='367')
  par_male = db.Column(db.Integer, db.CheckConstraint('par_male >= 3 AND par_male <= 6', name='check_hole_par_male'))
  si_male = db.Column(db.Integer, db.CheckConstraint('si_male >= 1 AND si_male <= 18', name='check_hole_si_male'))
  par_female = db.Column(db.Integer, db.CheckConstraint('par_female >= 3 AND par_female <= 6', name='check_hole_par_female'))
  si_female = db.Column(db.Integer, db.CheckConstraint('si_female >= 1 AND si_female <= 18', name='check_hole_si_female'))
  effective_date = db.Column(db.DATE, nullable=False, server_default=db.func.now())
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  @orm.validates('number')
  def validate_number(self, key, value):
      if not 1 <= value <= 18:
        raise ValueError(f'Invalid Hole Number - {value} - Hole Number must be between 1 and 18')
      return value

  @orm.validates('yards')
  def validate_yards(self, key, value):
      if not 0 <= value <= 999:
        raise ValueError(f'Invalid Yards - {value} - Length(yds) must be between 1 and 999')
      return value

  @orm.validates('meters')
  def validate_meters(self, key, value):
      if not 0 <= value <= 999:
        raise ValueError(f'Invalid Meters - {value} - Length(m) must be between 1 and 999')
      return value

  @orm.validates('par_male')
  @orm.validates('par_female')
  def validate_hole_par(self, key, value):
      if not 3 <= value <= 6:
        raise ValueError(f'Invalid Hole Par - {value} - Par must be between 3 and 6 for a hole')
      return value

  @orm.validates('si_male')
  @orm.validates('si_female')
  def validate_hole_si(self, key, value):
      if not 1 <= value <= 18:
        raise ValueError(f'Invalid Stroke Index - {value} - Stroke Index must be between 1 and 18 for a hole')
      return value

  def __init__(self, hole_id, tee_id=None, number=None, yards=None, meters=None, par_male=None, si_male=None, par_female=None, si_female=None, effective_date=None, created_at=None, updated_at=None):
    self.hole_id = hole_id
    self.tee_id = tee_id
    self.number = number
    self.yards = yards
    self.meters = meters
    self.par_male = par_male
    self.si_male = si_male
    self.par_female = par_female
    self.si_female = si_female
    self.effective_date = effective_date

  def as_dict(self):
    keys = ['created_at', 'updated_at']
    return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in keys}
