from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from app.extensions import db, cors

# FACILITY MODELS
from app.models import facility, course, tee, course_rating, hole, hole_geo, facility_season
# PERSON MODELS
from app.models import person
# EQUIPMENT MODELS
from app.models import equipment, equipment_spec, equipment_distance
# HANDICAP MODELS
from app.models import handicap_history
# ROUND MODELS
from app.models import round, round_score, round_hole, round_handicap, strokes_gained

from config import Config
 
def create_app(config_class=Config):
  app = Flask(__name__)

  # Set Config varibles
  app.config.from_object(config_class)

  # Initialize Flask extensions
  db.init_app(app)
  cors = CORS(app, resources={r'/*'})   

  # Mirgrate Models
  Migrate(app, facility.db)
  Migrate(app, course.db)
  Migrate(app, tee.db)
  Migrate(app, course_rating.db)
  Migrate(app, hole.db)
  Migrate(app, hole_geo.db) 
  Migrate(app, facility_season.db) 
  Migrate(app, facility_season.db) 
  Migrate(app, person.db)
  Migrate(app, equipment.db)
  Migrate(app, equipment_spec.db)
  Migrate(app, equipment_distance.db)
  Migrate(app, handicap_history.db)
  Migrate(app, strokes_gained.db)
  Migrate(app, round.db)
  Migrate(app, round_score.db)
  Migrate(app, round_handicap.db)
  Migrate(app, round_hole.db)

  # Register Blueprints
  # FACILITY BLUEPRINTS
  from app.facility import bp as facility_bp
  app.register_blueprint(facility_bp)
  from app.course import bp as course_bp
  app.register_blueprint(course_bp)
  from app.tee import bp as tee_bp
  app.register_blueprint(tee_bp)
  from app.hole import bp as hole_bp
  app.register_blueprint(hole_bp)
  from app.course_rating import bp as course_rating_bp
  app.register_blueprint(course_rating_bp)
  from app.hole_geo import bp as hole_geo_bp
  app.register_blueprint(hole_geo_bp)

  # PERSON BLUEPRINTS
  from app.person import bp as person_bp
  app.register_blueprint(person_bp)

  # EQUIPMENT BLUEPRINTS
  from app.equipment import bp as equipment_bp
  app.register_blueprint(equipment_bp)

  # HANDICAP BLUEPRINTS
  from app.handicap import bp as handicap_bp
  app.register_blueprint(handicap_bp)

  # SEEDER BLUEPRINT
  from app.seeders import bp as seeder_bp
  app.register_blueprint(seeder_bp)

  @app.route('/')
  def hello_world():
      return '<p>Hello, World!</p>'
  
  return app