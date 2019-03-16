from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/home')
def home():
	return render_template('home.html')
	
@app.route('/map')
def map():
	return render_template('map.html')

@app.route('/login')
def login():
	return render_template('login.html')
	
@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/donate')
def donate():
	return render_template('donate.html')

@app.route('/online')
def online():
	return render_template('online.html')

@app.route('/posts')
def posts():
	return render_template('posts.html')
	
@app.route('/contacts')
def contacts():
	return render_template('contacts.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run()