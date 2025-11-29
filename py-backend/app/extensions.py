from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import timedelta

from config import Config

db = SQLAlchemy()
#  Object Relational Mapper
orm = db.orm

# DB Engine
Engine = db.create_engine(
  Config.SQLALCHEMY_DATABASE_URI,
  pool_size=20,
  max_overflow=5
)

# CORS
cors = CORS()