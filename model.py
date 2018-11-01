from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Animals(Base):
	__tablename__ = 'animals'
	Id = Column(Integer , primary_key = True)
	name = Column(String)
	age = Column(Integer)
	Type = Column (String)
	finished_lab = Column(Boolean)
