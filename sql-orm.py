from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# Create a class base model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True),
    Name = Column(String)
)

# Create a class base model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True),
    Title = Column(String),
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))
)

# Create a class base model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True),
    Name = Column(String),
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId")),
    MediaTypeId = Column(Integer, primary_key=False),
    GenreId = Column(Integer, primary_key=False),
    Composer = Column(String),
    Milliseconds = Column(Integer),
    Bytes = Column(Integer),
    UnitPrice = Column(Float)
) 


# Instead of connecting to the database directly, a session is requested
# Create a new instance of sessionmaker, then point to the engine
Session = sessionmaker(db)
# Open an actual session by calling the Session() sbbclass defined above
session = Session()

# Create the database using declarative-base subclass
base.metadata.create_all(db)

