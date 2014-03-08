from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime

import datetime
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None
Base = declarative_base()

### Class declarations go here

class User(Base):
	__tablename__ = "users" #name of the table 

	id = Column(Integer, primary_key = True) #adds a column 'id', with an integer and it willbe the primary key
	email = Column(String(64), nullable=True) #this column is optional
	password = Column(String(64), nullable=True)
	age = Column(String(15), nullable=True)
	zipcode = Column(String(15), nullable=True)

class Movie(Base):
	__tablename__ = "Movies"
	
	id = Column(Integer, primary_key = True)
	name = Column(String(75))
	released_at = Column(DateTime(), nullable = True)
	imdb_url = Column(String(300), nullable = True)

class Rating(Base):
	__tablename__ = "Ratings"

	id = Column(Integer, primary_key = True)
	movie_id = Column(Integer, nullable = True)
	user_id = Column(Integer, nullable = True)
	rating = Column(Integer, nullable = True)


### End class declarations



def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()  #this instantiates the session

    #to instantiate sessions later: session = Session()



def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
