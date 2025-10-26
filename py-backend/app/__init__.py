from flask import Flask

from config import Config

def create_app(config_class=Config):
  app = Flask(__name__)

  # Set Config varibles
  app.config.from_object(config_class)

  # Register Blueprints
  from app.facility import bp as facility_bp
  app.register_blueprint(facility_bp)
 
  @app.route('/')
  def hello_world():
      return '<p>Hello, World!</p>'

  return app