import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
  ENV = os.environ.get('ENV')
  PORT = os.environ.get('PORT')
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

  GHIN_TOKEN = os.environ.get('GHIN_TOKEN')
  GHIN_BASE_URL = os.environ.get('GHIN_BASE_URL')
  GHIN_SCORES_ENDPOINT = os.environ.get('GHIN_SCORES_ENDPOINT')
  GHIN_COURSE_ENDPOINT = os.environ.get('GHIN_COURSE_ENDPOINT')
  GHIN_HANDICAP_ENDPOINT = os.environ.get('GHIN_HANDICAP_ENDPOINT')


  def __init__(self, **kwargs):
    super().__init__(**kwargs) 
