import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
  ENV = os.environ.get('ENV')
  PORT = os.environ.get('PORT')
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')


  def __init__(self, **kwargs):
    super().__init__(**kwargs) 
