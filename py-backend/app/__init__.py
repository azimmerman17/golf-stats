from flask import Flask
from flask_migrate import Migrate

from app.extensions import db

# FACILITY MODELS
from app.models import facility, course, tee, course_rating, hole, hole_geo, facility_season

from config import Config

def create_app(config_class=Config):
  app = Flask(__name__)

  # Set Config varibles
  app.config.from_object(config_class)

  # Initialize Flask extensions
  db.init_app(app)

  # Mirgrate Models
  Migrate(app, facility.db)
  Migrate(app, course.db)
  Migrate(app, tee.db)
  Migrate(app, course_rating.db)
  Migrate(app, hole.db)
  Migrate(app, hole_geo.db) 
  Migrate(app, facility_season.db) 

  # Register Blueprints
  #FACILITY BLUEPRINTS
  from app.facility import bp as facility_bp
  app.register_blueprint(facility_bp)
  from app.course import bp as course_bp
  app.register_blueprint(course_bp)
  from app.tee import bp as tee_bp
  app.register_blueprint(tee_bp)
  from app.hole import bp as hole_bp
  app.register_blueprint(hole_bp)

 
  @app.route('/')
  def hello_world():
      return '<p>Hello, World!</p>'

  return app