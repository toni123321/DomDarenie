from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
	fname = db.Column(db.String(100), nullable = False)
	sname = db.Column(db.String(100), nullable = False)
	email = db.Column(db.String(100), nullable = False) 
	username = db.Column(db.String(100), nullable = False)
	password = db.Column(db.String(100), nullable = False)

	def __init_(self, fname, sname, email, username, password):
		self.fname = fname
		self.sname = sname
		self.username = username
		self.email = email
		self.password = password

class Dom(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
	name = db.Column(db.String(100), nullable = False)
	address = db.Column(db.String(100), nullable = False)
	email = db.Column(db.String(100), nullable = False)
	password = db.Column(db.String(100), nullable = False)

	def __init_(self, name, address, email, password):
		self.name = name
		self.address = address
		self.email = email
		self.password = password

