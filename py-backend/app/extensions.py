from flask_sqlalchemy import SQLAlchemy

from config import Config

# Initalize DB
db = SQLAlchemy()

#  Object Relational Mapper
orm = db.orm

# DB Engine
Engine = db.create_engine(
  Config.SQLALCHEMY_DATABASE_URI,
  pool_size=20,
  max_overflow=5
)