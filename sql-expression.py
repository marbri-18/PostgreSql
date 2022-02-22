from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Executing the instructions from our localhost "Chinook" database
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# Create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# Create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


# Making the connection
with db.connect() as connection:

    # Query 1 - Select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - Select only the "Name" column from the "Artist" table
    select_query = artist_table.select().with_only_columns([artist_table.c.Name])


    results = connection.execute(select_query)
    for result in results:
        print(result)
