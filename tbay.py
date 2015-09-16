from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Engine will talk directly to your database using the raw SQL commands.
engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
#This is the equivalent to a psycopg2 cursor - it allows you to queue up and execute database transactions
Session = sessionmaker(bind=engine)
session = Session()
#This acts like a repository for the models, and will issue the create table statements to build up the database's table structure.
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float

#The Item model is represented by a class called Item
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
class User(Base): 
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Bid(Base):
    __tablename__ = "bid"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)




angela = User()
angela.username = "awoodall"
angela.password = "professor"
session.add(angela)
session.commit()

Base.metadata.create_all(engine)