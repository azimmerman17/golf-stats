import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
  ENV = os.environ.get('ENV')
  PORT = os.environ.get('PORT')

  def __init__(self, **kwargs):
    super().__init__(**kwargs) 
