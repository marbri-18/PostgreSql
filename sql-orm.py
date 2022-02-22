from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# Instead of connecting to the database directly, a session is requested
# Create a new instance of sessionmaker, then point to the engine
Session = sessionmaker(db)
# Open an actual session by calling the Session() sbbclass defined above
session = Session()

# Create the database using declarative-base subclass
base.metadata.create_all(db)