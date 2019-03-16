from flask import Flask, render_template, flash, request
import sqlite3


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
	"""msga = "initial msg"
	try:   			
   		with sqlite3.connect("database.db") as con:
   			cur = con.cursor()
   			cur.execute("select * from user")
   			con.execute("INSERT INTO user (fname, sname, email, username, password) VALUES ('Gosho', 'Goshev', 'goshko@abv', 'goshev', 'neshto')")
   			con.commit()
   			msga = "Record succesfully added"
   			msga = cur.fetchall()


   	except:
   		con.rollback()
   		msga = "error"

   	finally:
   		return render_template('result.html', msg = msga)
   		con.close()"""
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
   		try:
   			fn = request.form['fname']
   			sn = request.form['sname']
   			us = request.form['username']
   			em = request.form['email']
   			ps = request.form['password']

   			with sqlite3.connect("database.db") as con:
   				cur = con.cursor()
   				cur.execute("INSERT INTO user (fname, sname, email, username, password) VALUES (?, ?, ?, ?, ?)", (fn, sn, em, us, ps) )
   				con.commit()
   				msga = "Record succesfully added"

   		except:
   			con.rollback()
   			msga = "error"

   		finally:
   			con.close()



if __name__ == '__main__':
   app.run()