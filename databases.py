from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_animal(name, age , Type, finshed_lab):
  animals_object = Animals(
  	name= name,
  	age=age,
  	Type=Type,
  	finshed_lab=finshed_lab)
  session.add(animals_object)
  session.commit()

def update_animal_name(name, ):
  animals_object= session.query(
  	animals).filter_by(
  	name=name).first()

   session.commit()

def delete_animals(name):
   session.query(Animals).filter_by(
       name=name).delete()
   session.commit()


# def get_product(Id):
#    animals = session.query(
#        Animals).filter_by(
#        Id=Id).first()
#     print (Animals)

create_animal("ww",1,"mm",True)

