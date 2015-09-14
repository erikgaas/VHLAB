from sqlalchemy import create_engine, ForeignKey
from sqlqlchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('sqlite:///:memory:', echo=True))

Base = declarative_base()


#Consider including the repr functions because that might be nice.
class Heart_Hist(Base):
	__tablename__ = 'heart_hist'

	heart_number = Column(String, primary_key=True)
	sex = Column(String, Enum('F', 'M'))
	age = Column(Integer)
	bmi = Column(Integer)
	weight = Column(Float)
	height = Column(Integer)


class Cardiac_Disease(Base):
	__tablename__ = 'cardiac_disease'
	id = Column(Integer, primary_key=True)
	heart_number = Column(String, ForeignKey('Heart_Hist.heart_number'))
	years = Column(Integer)
	severity = Column(String, Enum('mild', 'moderate', 'severe'))

	heart_hist = relationship("Heart_Hist", backref=backref('cardiac_diseases', order_by=id))

class Systemic_Diseases(Base):
	__tablename__ = 'systemic_diseases'

	id = Column(Integer, primary_key=True)
	heart_number = Column(String, ForeignKey('Heart_Hist.heart_number'))
	years = Column(Integer)
	severity = Column(String, Enum('mild', 'moderate', 'severe'))

	heart_hist = relationship("Heart_Hist", backref=backref('systemic_diseases', order_by=id))

#class Region_Group(Base):

#class Region(Base):

#class Group_To_Region

#class Media(Base):

#class Media_To_Region

#class Blood_Tissue_Model

#class Coronary_Model


Session = sessionmaker(bind=engine)
session = Session()


