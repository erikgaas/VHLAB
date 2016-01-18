import flask
import flask.ext.sqlalchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

class Specimen(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	identifier = db.Column(db.Unicode, unique=True)
	sex = db.Column(db.Unicode, db.Enum('F', 'M'))
	age = db.Column(db.Integer)
	bmi = db.Column(db.Integer)
	weight = db.Column(db.Float)
	height = db.Column(db.Integer)
	cardiac_hist = db.Column(db.Unicode)
	systemic_hist = db.Column(db.Unicode)
	comment = db.Column(db.Unicode)

class Macro_Region(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode)
	description = db.Column(db.Unicode)
	img_path = db.Column(db.Unicode)

	micro_regions = db.relationship('Micro_Region',
		backref=db.backref('Parent_Region', lazy='joined'))

class Micro_Region(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode)
	description = db.Column(db.Unicode)
	img_path = db.Column(db.Unicode)


db.create_all()