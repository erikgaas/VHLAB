from sqlalchemy import Column, Integer, String, Enum, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()

class Heart(Base):
	__tablename__ = 'heart'

	id = Column(Integer, primary_key=True)
	heart_name = Column(String(10))
	sex = Column(String(10), Enum('M', 'F'))
	age = Column(Integer)
	bmi = Column(Float)
	weight = Column(Float)
	height = Column(Float)
	cardiac_hist = Column(Text)
	systemic_hist = Column(Text)
	comment = Column(Text)

	media = relationship('Media', backref='heart')

	@property
	def serialize(self):
	    return {
	    	'id': self.id,
	    	'heart_name': self.heart_name,
	    	'sex': self.sex,
	    	'age': self.age,
	    	'bmi': self.bmi,
	    	'weight': self.weight,
	    	'height': self.height,
	    	'cardiac_hist': self.cardiac_hist,
	    	'systemic_hist': self.systemic_hist,
	    	'comment': self.comment
	    }

class LargeRegion(Base):
	__tablename__ = 'large_region'

	id = Column(Integer, primary_key=True)
	name = Column(String(30))
	description = Column(Text)
	media_id = Column(Integer, ForeignKey('media.id'))

	small_regions = relationship('SmallRegion', backref="large_region")

	@property
	def serialize(self):
	    return {
	    	'id': self.id,
	    	'name': self.name,
	    	'small_regions': str([i.serialize for i in self.small_regions]),#[i.serialize() for i in self.small_regions],
	    	'description': self.description,
	    	'media_id': self.media_id
	    }
	

class SmallRegion(Base):
	__tablename__ = 'small_region'

	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	large_region_id = Column(Integer, ForeignKey('large_region.id'))
	description = Column(Text)
	media_id = Column(Integer, ForeignKey('media.id'))

	media = relationship(Integer, backref='small_region')

	@property
	def serialize(self):
	    return {
	    	'id': self.id,
	    	'name': self.name,
	    	'description': self.description
	    }


class ImageMode(Base):
	__tablename__ = 'image_mode'

	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	description = Column(Text)
	media_id = Column(Integer, ForeignKey('media.id'))

	image_targets = relationship('ImageTarget', backref="image_mode")

	@property
	def serialize(self):
	    return {
	    	'id': self.id,
	    	'name': self.name,
	    	'description': self.description
	    }
	
class ImageTarget(Base):
	__tablename__ = 'image_target'

	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	description = Column(Text)
	image_mode_id = Column(Integer, ForeignKey('image_mode.id'))
	media_id = Column(Integer, ForeignKey('media.id'))


	@property
	def serialize(self):
	    return {
	    	'id': self.id,
	    	'name': self.name,
	    	'description': self.description
	    }
	



class Media(Base):
	__tablename__ = 'media'

	id = Column(Integer, primary_key=True)
	HN_ID = Column(Integer, ForeignKey('Hearts'), nullable=True)
	name = Column(String(50))
	video_source = Column(String(50))
	still_source = Column(String(50))
	#Dates?
	description = Column(Text)
	heart_type = Column(Enum('functional', "perf-fixed", "comp-img", "plate", "pre-plate", "graphic", "venous", "aterial", "combined", "hypertrophic", "dilated-cardiomyopathy", "normal", "pediatric"))

	large_region = relationship('LargeRegion', backref='media')
	small_region = relationship('SmallRegion', backref='media')
	image_mode = relationship('ImageMode', backref='media')
	image_target = relationship('ImageTarget', backref='media')

	@property
	def serialize(self):
	    return {
	    	'id': self.id,
	    	'name': self.name,
	    	'video_source': self.video_source,
	    	'still_source': self.still_source,
	    	'description': self.description,
	    	'heart_type': self.heart_type
	    }
	

	
class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	username = Column(String(32), index=True)
	password_hash = Column(String(64))

	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

engine = create_engine('sqlite:///vhlab.db')
Base.metadata.create_all(engine)