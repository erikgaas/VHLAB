import flask.ext.restless

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

specimen_blueprint = manager.create_api(Specimen, 
	methods=['GET'])

macro_region_blueprint = manager.create_api(Macro_Region,
	methods=['GET'])

micro_region_blueprint = manager.create_api(Micro_Region)