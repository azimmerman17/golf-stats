from datetime import date

from app.extensions import db, orm
from app.models.round import Round

# Model Contains Score information for Rounds Played
class Round_Score(db.Model):
  round_score_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  round_id = db.Column(db.Integer, db.ForeignKey(Round.round_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  gross_score = db.Column(db.Integer, nullable=False)
  net_score = db.Column(db.Integer, nullable=False)
  par = db.Column(db.Integer, nullable=False, server_default='72')
  to_par_value = db.Column(db.String, nullable=False)
  score_out = db.Column(db.Integer)
  par_out = db.Column(db.Integer)
  score_in = db.Column(db.Integer)
  par_in = db.Column(db.Integer)
  expected_score = db.Column(db.Float)
  expected_score_in = db.Column(db.Float)
  expected_score_out = db.Column(db.Float)
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())


  def __init__(self, round_score_id=None, round_id=None, gross_score=None, net_score=None, par=None, to_par_value=None, score_out=None, par_out=None, score_in=None, par_in=None, expected_score=None, expected_score_in=None, expected_score_out=None, created_at=None, updated_at=None):
    self.round_score_id = round_score_id
    self.round_id = round_id
    self.gross_score = gross_score
    self.net_score = net_score
    self.par = par
    self.to_par_value = to_par_value
    self.score_out = score_out
    self.par_out = par_out
    self.score_in = score_in
    self.par_in = par_in
    self.expected_score = expected_score
    self.expected_score_in = expected_score_in
    self.expected_score_out = expected_score_out
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
    INSERT INTO "Round_Score" ({keys})
    VALUES ({values})
    ;"""

    return query

  def update_row(self, update_dict):
    query = """
    UPDATE "Round_Score"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key}='{update_dict[key]}'"
    
    query = f"""{query}
    WHERE {f"round_score_id = {self.round_id}"}
    ;"""

    return  query

  def delete_row(self):
    query = f"""
    DELETE FROM "Round_Score" 
    WHERE {f"round_score_id = {self.round_id}"}
    ;"""

    return query
