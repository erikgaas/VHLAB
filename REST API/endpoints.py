from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Heart, LargeRegion, SmallRegion


from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)



engine = create_engine('sqlite:///vhlab.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#Admin stuff here 
#=================
admin = Admin(app, name='vhlab', template_mode="bootstrap3")
admin.add_view(ModelView(Heart, session))
admin.add_view(ModelView(LargeRegion, session))
admin.add_view(ModelView(SmallRegion, session))

#========================




@app.route("/hearts")
def hearts():
	return getAllHearts()

@app.route("/large_regions")
def large_regions():
	return getAllLargeRegions()

@app.route("/small_regions")
def small_regions():
	return getAllSmallRegions()


def getAllHearts():
	hearts = session.query(Heart).all()
	return jsonify(Hearts=[i.serialize for i in hearts])

def getAllLargeRegions():
	large_regions = session.query(LargeRegion).all()
	return jsonify(Large_Regions=[i.serialize for i in large_regions])

def getAllSmallRegions():
	small_regions = session.query(SmallRegion).all()
	return jsonify(Small_Regions=[i.serialize for i in small_regions])


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5555)