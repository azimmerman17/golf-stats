from app.extensions import db, orm
from app.models.person import Person


class Handicap_History(db.Model):
  handicap_history_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  person_id = db.Column(db.Integer, db.ForeignKey(Person.person_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  ghin_number = db.Column(db.String(10), db.ForeignKey(Person.ghin_number, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  assoc = db.Column(db.String(25))
  club = db.Column(db.String(50))
  hard_soft_cap = db.Column(db.String(3), nullable=False, server_default= 'N')
  hard_cap = db.Column(db.String(3), nullable=False, server_default= 'N')
  soft_cap = db.Column(db.String(3), nullable=False, server_default= 'N')
  rev_date = db.Date()
  hi_displsy = db.Column(db.String(5))
  hi_value = db.Column(db.String(5))
  low_h_displsy = db.Column(db.String(5))
  low_hi_value = db.Column(db.String(5))
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  def __init__(self,handicap_history_id=None, person_id=None, ghin_number=None, assoc=None, club=None, hard_soft_cap=None, hard_cap=None, soft_cap=None, rev_date=None, hi_displsy=None, hi_value=None, low_h_displsy=None, low_hi_value=None, created_at=None, updated_at=None):
    self.handicap_history_id = handicap_history_id
    self.person_id = person_id
    self.ghin_number = ghin_number
    self.assoc = assoc
    self.club = club
    self.hard_soft_cap = hard_soft_cap
    self.hard_cap = hard_cap
    self.soft_cap = soft_cap
    self.rev_date = rev_date
    self.hi_displsy = hi_displsy
    self.hi_value = hi_value
    self.low_h_displsy = low_h_displsy
    self.low_hi_value = low_hi_value
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
    INSERT INTO "Handicap_History" ({keys})
    VALUES ({values})
    ;"""

    return query

  def update_row(self, update_dict):
    query = """
    UPDATE "Handicap_History"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key}='{update_dict[key]}'"
    
    query = f"""{query}
    WHERE {f"handicap_history_id = {self.handicap_history_id}" if self.handicap_history_id is not None else ""}
    ;"""

    return  query

  def delete_row(self):
    query = f"""
    DELETE FROM "Handicap_History" 
    WHERE {f"handicap_history_id = {self.handicap_history_id}" if self.handicap_history_id is not None else ""}
    ;"""

    return query

