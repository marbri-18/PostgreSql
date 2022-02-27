from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

   
 


# Instead of connecting to the database directly, a session is requested
# Create a new instance of sessionmaker, then point to the engine
Session = sessionmaker(db)
# Open an actual session by calling the Session() sbbclass defined above
session = Session()

# Create the database using declarative-base subclass
base.metadata.create_all(db)