import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
  TEST = os.environ.get('TEST')
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
  PORT = os.environ.get('PORT')
  PEPPER = os.environ.get('PEPPER')
  ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY')
  JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
  JWT_TOKEN_LOCATION = os.environ.get('JWT_TOKEN_LOCATION')
  JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES')
  FRONTEND_URL = os.environ.get('FRONTEND_URL')