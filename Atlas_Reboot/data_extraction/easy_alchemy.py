from sqlalchemy import create_engine, ForeignKey, Table, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, TIMESTAMP
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('sqlite:///:memory:', echo=True)

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
	comment = Column(String)


class Cardiac_Disease(Base):
	__tablename__ = 'cardiac_disease'
	id = Column(Integer, primary_key=True)
	heart_number = Column(String, ForeignKey('Heart_Hist.heart_number'))
	years = Column(Integer)
	severity = Column(String, Enum('mild', 'moderate', 'severe'))
	comment = Column(String)

	heart_hist = relationship("Heart_Hist", backref=backref('cardiac_diseases', order_by=id))

#Consider adding table only for cardiac diseases

class Systemic_Diseases(Base):
	__tablename__ = 'systemic_diseases'

	id = Column(Integer, primary_key=True)
	heart_number = Column(String, ForeignKey('Heart_Hist.heart_number'))
	years = Column(Integer)
	severity = Column(String, Enum('mild', 'moderate', 'severe'))
	comment = Column(String)

	heart_hist = relationship("Heart_Hist", backref=backref('systemic_diseases', order_by=id))

#Consider adding table only for systemic diseases.

group_to_regions = Table('group_to_regions', Base.metadata,
	Column('group_id', Integer, ForeignKey('Region_Group.id')),
	Column('region_id', Integer, ForeignKey('Region.id'))
	)

class Region_Group(Base):
	__tablename__ = 'region_group'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	img_path = Column(String)

	regions = relationship('Region', secondary=group_to_regions, backref='regions')
	#need group_regions

region_to_media = Table('region_to_media', Base.metadata,
	Column('region_id', Integer, ForeignKey('Region.id')),
	Column('media_id', Integer, ForeignKey('Media.id'))
	)


class Region(Base):
	__tablename__ = 'region'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	img_path = Column(String)

	medias = relationship('Media', secondary=region_to_media, backref='region_media')
	#need region_to_media

class Media(Base):
	__tablename__ = 'media'

	id = Column(Integer, primary_key=True)
	item_name = Column(String)
	media_type = Column(String)
	date_created = Column(TIMESTAMP)
	date_modified = Column(TIMESTAMP)
	file_name = Column(String)
	description = Column(String)
	rendered_flag = Column(Boolean)
	labeled_flag = Column(Boolean)
	html5_flag = Column(Boolean)
	flag1 = Column(Boolean)
	flag2 = Column(Boolean)
	comment = Column(String)

	heart_state = Column(String, Enum('functional', 'pre-fixed', 'fixed'))
	img_type = Column(String, Enum('endoscope', 'external_img', 'mir', '3dmodel', 'comp_img'))

class Blood_Tissue_Model(Base):
	__tablename__ = 'blood_tissue_model'

	id = Column(Integer, primary_key=True)
	media_id = Column(String, ForeignKey('Media.id'))
	heart_state = Column(String, Enum('Hypertrophic', 'Dilated Cardiomyopathy', 'Normal', 'Pediatric'))

	blood_tissue_models = relationship('Media', backref=backref('blood_tissue_models', order_by=id))


class Coronary_Model(Base):
	__tablename__ = 'coronary_model'
	id = Column(String, primary_key=True)
	media_id = Column(String, ForeignKey('Media.id'))
	coronary_view = Column(String, Enum('Venous', 'Arterial', 'Combined'))

	coronary_models = relationship('Media', backref=backref('coronary_models', order_by=id))

Session = sessionmaker(bind=engine)
session = Session()


