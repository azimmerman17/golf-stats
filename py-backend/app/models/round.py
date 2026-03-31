from datetime import date

from app.extensions import db, orm
from app.models.course import Course
from app.models.tee import Tee
from app.models.course_rating import Course_Rating
from app.models.person import Person


# Model Contains Base information for Rounds Played
class Round(db.Model):
  round_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  ghin_id = db.Column(db.Integer, unique=True)
  third_party_id = db.Column(db.Integer, unique=True)
  course_id = db.Column(db.Integer, db.ForeignKey(Course.course_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  third_party_course_id = db.Column(db.Integer, unique=True) # Need to add to the Course Model???
  tee_id = db.Column(db.Integer, db.ForeignKey(Tee.tee_id, onupdate="CASCADE", ondelete="CASCADE"))
  ghin_tee_id = db.Column(db.Integer) # Need to add to the Tee Model???
  third_party_tee_id = db.Column(db.Integer) # Need to add to the Tee Model???
  course_rating_id = db.Column(db.Integer, db.ForeignKey(Course_Rating.course_rating_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  person_id = person_id = db.Column(db.Integer, db.ForeignKey(Person.person_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  ghin_number = db.Column(db.String(10), db.ForeignKey(Person.ghin_number, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  person_ss_id = db.Column(db.String)
  course_name = db.Column(db.String, db.ForeignKey(Course.name, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  tee_name = db.Column(db.String, db.ForeignKey(Tee.name, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  round_date = db.Column(db.DATE, nullable=False, server_default=db.func.now())
  count_in_stats = db.Column(db.Boolean, nullable=False, server_default='t')
  count_in_hanicap = db.Column(db.Boolean, nullable=False, server_default='t')
  lock_round = db.Column(db.Boolean, nullable=False, server_default='f')
  holes_played = db.Column(db.Integer, db.CheckConstraint('holes_played >= 1 AND holes_played <= 18',  name='check_round_holes_played'), nullable=False, server_default='18')
  start_time = db.Column(db.Time)
  end_time = db.Column(db.Time)
  total_time = db.Column(db.Time)
  transportation = db.Column(db.Enum('W','C','P','M', 'O', name='Round_Transportation'), nullable=False, server_default='W')
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  @orm.validates('holes_played')
  def validate_course_count(self, key, value):
    if value != None: 
      if value <= 0:
        raise ValueError(f'Invalid Holes Played - {value} - A round must have between 1 and 18 holes')
    return value

  def __init__(self, third_party_id=None, course_id=None, third_party_course_id=None, tee_id=None, ghin_tee_id=None, third_party_tee_id=None, course_rating_id=None, person_id=None, ghin_number=None, person_ss_id=None, course_name=None, tee_name=None, round_date=None, count_in_stats=None, count_in_hanicap=None, lock_round=None, holes_played=None, start_time=None, end_time=None, total_time=None, transportation=None, created_at=None, updated_at=None):
    self.round_id = round_id
    self.ghin_id = ghin_id
    self.third_party_id = third_party_id
    self.course_id = course_id
    self.third_party_course_id = third_party_course_id
    self.tee_id = tee_id
    self.ghin_tee_id = ghin_tee_id
    self.third_party_tee_id = third_party_tee_id
    self.course_rating_id = course_rating_id
    self.person_id = person_id
    self.ghin_number = ghin_number
    self.person_ss_id = person_ss_id
    self.course_name = course_name
    self.tee_name = tee_name
    self.round_date = round_date
    self.count_in_stats = count_in_stats
    self.count_in_hanicap = count_in_hanicap
    self.lock_round = lock_round
    self.holes_played = holes_played
    self.start_time = start_time
    self.end_time = end_time
    self.total_time = total_time
    self.transportation = transportation
    self.created_at = created_at
    self.updated_at = updated_at

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
    INSERT INTO "Round" ({keys})
    VALUES ({values})
    ;"""

    return query

  def update_row(self, update_dict):
    query = """
    UPDATE "Round"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key}='{update_dict[key]}'"
    
    query = f"""{query}
    WHERE {f"round_id = {self.round_id}"}
    ;"""

    return  query

  def delete_row(self):
    query = f"""
    DELETE FROM "Round" 
    WHERE {f"round_id = {self.round_id}"}
    ;"""

    return query

