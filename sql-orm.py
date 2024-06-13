from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from out localhost "chinook" db
db = create_engine("postgresql://postgres:Li1357924680il@localhost:5432/chinook" )
base = declarative_base()

# create a class-based model for the "Artist" table
class ArtistTable(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    
# create a class-based model for the "Album" table
class AlbumTable(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("ArtistTable.ArtistId"))
    
# create a class-based model for  the "Track" table
class TrackTable(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("AtristTable.ArtwistId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)
    
# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the "Artist" table
# artists = session.query(ArtistTable)
# for artist in artists:
#    print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(ArtistTable)
# for artist in artists:
#   print(artist.Name)
   
# Query 3 - select onle "Queen" from the "Artist" table
# artist = session.query(ArtistTable).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 fomr the "Artist" table
# artist = session.query(ArtistTable).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select onle the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(AlbumTable).filter_by(ArtistId=51)
# for album in albums:
#   print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")
    
# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(TrackTable).filter_by(Composer="Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId, track.MediaTypeId, track.GenreId, track.Composer, track.Milliseconds, track.Bytes, track.UnitPrice, sep=" | ")