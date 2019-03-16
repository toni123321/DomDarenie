from flask import Flask, render_template, flash, request
import sqlite3


app = Flask(__name__)

class User_login:
	logged_in = False

	def is_login(self):
		return self.logged_in

	def login(self):
		self.logged_in = True

	def logout(self):
		self.logged_in = False

user_l = User_login()

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/home')
def home():
	return render_template('home.html')
	
@app.route('/orphan_homes')
def orphan_homes():
	return render_template('orphan_homes.html')
		
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
	
@app.route('/donators')
def donate():
	return render_template('donators.html')

@app.route('/online')
def online():
	return render_template('online.html')

	
@app.route('/contacts')
def contacts():
	return render_template('contacts.html')

@app.route('/result', methods = ['POST', 'GET'])
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
   			return render_template('result.html', msg = msga)


@app.route('/loggedin', methods = ['POST', 'GET'])
def loggedin():
	if request.method == 'POST':
		msga = "initial msg"
		try:
			us = request.form['username']
			ps = request.form['password']

			with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("select * from user WHERE username = ? AND password = ?", (us, ps))
				con.commit()

				if(cur.fetchone() == None):
					raise Exception()
				else:
					user_l.login()
					msga = us 
		except :
			con.rollback()
			msga = "Username and password don't match"
		finally:
			con.close()
			return render_template('loggedin.html', msg = user_l.is_login())


if __name__ == '__main__':
   app.run()
