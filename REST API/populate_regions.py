#from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Heart, LargeRegion, SmallRegion
#app = Flask(__name__)

engine = create_engine('sqlite:///vhlab.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

region_dict = {}
f = open('regions.txt', 'r'
large_regions = f.readline()[:-1].split(',')
for large_region in large_regions:
	small_regions = f.readline()[:-1].split(',')
	region_dict[large_region] = small_regions

def convert_name_to_movie(name):
	name = name.replace(' ', '-')
	name = name + "-starteimage"
	return name

#Get large regions in the db
for item in region_dict.items():
	name = item[0]
	graphics_url = convert_name_to_movie(name) #sans .mp4. Remember this!
	description = None
	graphics_type = 'video'
	session.add(LargeRegion(name=name, description=description, graphics_type=graphics_type, graphics_url=graphics_url))
	
session.commit()
print("large region successful")
for item in region_dict.items():
	large_name = item[0]
	large_id = session.query(LargeRegion).filter(LargeRegion.name==large_name).first().identifier
	for small_region in region_dict[large_name]:
		name = small_region
		description = None
		graphics_type = 'video'
		graphics_url = convert_name_to_movie(name)
		session.add(SmallRegion(name=name, large_region_id=large_id,
			description=description, graphics_type=graphics_type, graphics_url=graphics_url))

session.commit()