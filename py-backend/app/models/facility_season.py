from app.extensions import db, orm
from app.models.facility import Facility

# Model to define the length of a posting season for a facility
class Facility_Season(db.Model):
  __tablename__ = 'Facility_Season'
  
  facility_season_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  facility_id = db.Column(db.Integer, db.ForeignKey(Facility.facility_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False, unique=True)
  start_date = db.Column(db.String(50))
  end_date = db.Column(db.String(50))
  year_round = db.Column(db.Boolean, nullable=False, server_default='0')
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

  def __init__(self, **kwargs):
    super().__init__(**kwargs) 