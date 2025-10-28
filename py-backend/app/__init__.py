from flask import Flask
from flask_migrate import Migrate

from app.extensions import db

# FACILITY MODELS
from app.models import facility, course, tee

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



  # Register Blueprints
  from app.facility import bp as facility_bp
  app.register_blueprint(facility_bp)
 
  @app.route('/')
  def hello_world():
      return '<p>Hello, World!</p>'

  return app