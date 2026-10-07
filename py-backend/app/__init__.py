from flask import Flask

from config import Config

def create_app(config_class=Config):
  app = Flask(__name__)

  # Set Config varibles
  app.config.from_object(config_class)

  # Initialize Flask extensions

  # Mirgrate Models

  # Register Blueprints

  @app.route('/')
  def hello_world():
      return f'<p>Welcome to the {config_class.ENV} Golf Stats Server</p>'
  
  return app