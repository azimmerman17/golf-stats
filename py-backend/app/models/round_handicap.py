from datetime import date

from app.extensions import db, orm
from app.models.round import Round

# Model Contains Handicap information for Rounds Played
class Round_Handicap(db.Model):
  round_handicap_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  round_id = db.Column(db.Integer, db.ForeignKey(Round.round_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  gross_score = db.Column(db.Integer, nullable=False)
  esc_score = db.Column(db.Integer, nullable=False)
  holes_played = db.Column(db.Integer, nullable=False)
  differential = db.Column(db.Float)
  course_rating = db.Column(db.Float)
  slope_rating = db.Column(db.Integer)
  course_handicap = db.Column(db.Integer)
  pcc = db.Column(db.Float)
  gender = db.String(1)
  exceptional = db.Column(db.Boolean, nullable=False, server_default='f')
  net_differential = db.Column(db.Float)
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  def __init__(self, round_handicap_id=None, round_id=None, gross_score=None, esc_score=None, holes_played=None, differential=None, course_rating=None, slope_rating=None, course_handicap=None, pcc=None, gender=None, exceptional=None, net_differential=None, created_at=None, updated_at=None):
    self.round_handicap_id = round_handicap_id
    self.round_id = round_id
    self.gross_score = gross_score
    self.esc_score = esc_score
    self.holes_played = holes_played
    self.differential = differential
    self.course_rating = course_rating
    self.slope_rating = slope_rating
    self.course_handicap = course_handicap
    self.pcc = pcc
    self.gender = gender
    self.exceptional = exceptional
    self.net_differential = net_differential
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
    INSERT INTO "Round_Handicap" ({keys})
    VALUES ({values})
    ;"""

    return query

  def update_row(self, update_dict):
    query = """
    UPDATE "Round_Handicap"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key}='{update_dict[key]}'"
    
    query = f"""{query}
    WHERE {f"round_handicap_id = {self.round_handicap_id}"}
    ;"""

    return  query

  def delete_row(self):
    query = f"""
    DELETE FROM "Round_Handicap" 
    WHERE {f"round_handicap_id = {self.round_handicap_id}"}
    ;"""

    return query
