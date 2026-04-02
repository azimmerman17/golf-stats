from datetime import date

from app.extensions import db, orm
from app.models.round import Round
from app.models.hole import Hole


# Model Contains Hole information for Rounds Played
class Round_Hole(db.Model):
  round_hole_id  = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  round_id = db.Column(db.Integer, db.ForeignKey(Round.round_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  hole_id =  db.Column(db.Integer, db.ForeignKey(Hole.hole_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  ghin_hole_id = db.Column(db.Integer)
  third_party_hole_id = db.Column(db.Integer)
  third_party_round_hole_id = db.Column(db.Integer)
  hole_number = db.Column(db.Integer, nullable=False)
  yardage = db.Column(db.Integer, nullable=False)
  par = db.Column(db.Integer, nullable=False)
  score = db.Column(db.Integer)
  score_vs_par = db.Column(db.String)
  expected_score = db.Column(db.Float)
  esc_score = db.Column(db.Integer)
  stroke_index = db.Column(db.Integer)
  x_hole = db.Column(db.Boolean, nullable=False, server_default='f')
  hole_catagory =db.Column(db.Enum('T3', 'S3', 'M3', 'L3', 'T4', 'S4', 'M4', 'L4', 'T5', 'S5', 'M5', 'L5', name='Round_Hole_Catagory'))
  tiger_five_errors = db.Column(db.ARRAY(db.Enum('A', 'B', 'C', 'D', 'E', name='Hole_Tiger_Five')))
  net_tiger_five_errors = db.Column(db.ARRAY(db.Enum('A', 'G', 'H', 'I', 'J', name='Hole_Net_Tiger_Five')))
  fairway_hit = db.Column(db.Boolean, nullable=False, server_default='f')
  drive_miss = db.Column(db.Enum('NW', 'N', 'NE', 'W', 'E', 'SW', 'S', 'SE', 'OW', 'OE' 'ON', 'OS', name='Round_Hole_Drive_Miss'))
  drive_lie = db.Column(db.Enum('F', 'R', 'S', 'X', 'G', 'P', 'H', 'FC', 'W', 'FR', name='Round_Hole_Drive_Lie'), nullable=False, server_default='F')
  approach_distance = db.Column(db.Integer)
  approach_lie = db.Column(db.Enum('T', 'F', 'R', 'S', 'X', 'G', 'P', 'H', 'FC', 'W', 'FR', name='Round_Hole_Approach_Lie'), nullable=False, server_default='F')
  prox_to_hole = db.Column(db.Integer)
  prox_to_hole_lie = db.Column(db.Enum('F', 'R', 'S', 'X', 'G', 'P', 'H', 'FC', 'W', 'FR', name='Round_Hole_Prox_To_Hole_Lie'), nullable=False, server_default='F')
  green_hit = db.Column(db.Boolean, nullable=False, server_default='f')
  green_miss = db.Column(db.Enum('NW', 'N', 'NE', 'W', 'E', 'SW', 'S', 'SE', 'OW', 'OE' 'ON', 'OS', name='Round_Hole_Green_Miss'))
  green_hit_plus_one = db.Column(db.Boolean, nullable=False, server_default='f')
  green_miss_lie =  db.Column(db.Enum('F', 'R', 'S', 'X', 'G', 'P', 'H', 'FC', 'W', 'FR', name='Round_Hole_Green_Miss_Lie'), nullable=False, server_default='F')
  putts = db.Column(db.Integer)
  tee_lat = db.Column(db.Float)
  tee_lon = db.Column(db.Float)
  turn_lat = db.Column(db.Float)
  turn_lon = db.Column(db.Float)
  pin_lat = db.Column(db.Float)
  pin_lon = db.Column(db.Float)
  start_time = db.Column(db.Time)
  end_time = db.Column(db.Time)
  time_per_shot = db.Column(db.Interval)
  sg_total = db.Column(db.Float)
  sg_tee = db.Column(db.Float)
  sg_approach = db.Column(db.Float)
  sg_short_game = db.Column(db.Float)
  sg_putting = db.Column(db.Float)
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  def __init__(self, round_hole_id=None, round_id=None, hole_id=None, ghin_hole_id=None, third_party_hole_id=None, third_party_round_hole_id=None, hole_number=None, par=None, score=None, score_vs_par=None, esc_score=None, stroke_index=None, x_hole=None, fairway_hit=None, drive_miss=None, drive_miss_lie=None, green_hit=None, green_miss=None, green_hit_plus_one=None, green_miss_lie=None, putts=None, expected_strokes=None, strokes_gained=None, tee_lat=None, tee_lon=None, pin_lat=None, pin_lon=None, turn_lat=None, turn_lon=None, start_time=None, end_time=None, time_per_shot=None, approach_distance=None, approach_lie=None, prox_to_hole=None, prox_to_hole_lie=None, expected_score=None, sg_total=None, sg_tee=None, sg_approach=None, sg_short_game=None, sg_putting=None, tiger_five_errors=None, hole_catagory=None, net_tiger_five_errors=None, created_at=None, updated_at=None):
    self.round_hole_id = round_hole_id
    self.round_id = round_id
    self.hole_id = hole_id
    self.ghin_hole_id = ghin_hole_id
    self.third_party_hole_id = third_party_hole_id
    self.third_party_round_hole_id = third_party_round_hole_id
    self.hole_number = hole_number
    self.par = par
    self.score = score
    self.score_vs_par = score_vs_par
    self.esc_score = esc_score
    self.stroke_index = stroke_index
    self.x_hole = x_hole
    self.fairway_hit = fairway_hit
    self.drive_miss = drive_miss
    self.drive_miss_lie = drive_miss_lie
    self.green_hit = green_hit
    self.green_miss = green_miss
    self.green_hit_plus_one = green_hit_plus_one
    self.green_miss_lie = green_miss_lie
    self.putts = putts
    self.expected_strokes = expected_strokes
    self.strokes_gained = strokes_gained
    self.tee_lat = tee_lat
    self.tee_lon = tee_lon
    self.pin_lat = pin_lat
    self.pin_lon = pin_lon
    self.turn_lat = turn_lat
    self.turn_lon = turn_lon
    self.start_time = start_time
    self.end_time = end_time
    self.time_per_shot = time_per_shot
    self.approach_distance = approach_distance
    self.approach_lie = approach_lie
    self.prox_to_hole = prox_to_hole
    self.prox_to_hole_lie = prox_to_hole_lie
    self.expected_score = expected_score
    self.sg_total = sg_total
    self.sg_tee = sg_tee
    self.sg_approach = sg_approach
    self.sg_short_game = sg_short_game
    self.sg_putting = sg_putting
    self.tiger_five_errors = tiger_five_errors
    self.net_tiger_five_errors = net_tiger_five_errors
    self.hole_catagory = hole_catagory
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
    INSERT INTO "Round_Hole" ({keys})
    VALUES ({values})
    ;"""

    return query

  def update_row(self, update_dict):
    query = """
    UPDATE "Round_Hole"
    SET updated_at = NOW()"""

    for key in update_dict.keys():
      query = f"{query}, {key}='{update_dict[key]}'"
    
    query = f"""{query}
    WHERE {f"round_hole_id = {self.round_hole_id}"}
    ;"""

    return  query

  def delete_row(self):
    query = f"""
    DELETE FROM "Round_Hole" 
    WHERE {f"round_hole_id = {self.round_hole_id}"}
    ;"""

    return query
