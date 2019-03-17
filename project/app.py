from flask import Flask, render_template, flash, request
import sqlite3


app = Flask(__name__)

class User_login:
	logged_in = False
	username = None
	fname = None
	sname = None
	email = None

	def is_login(self):
		return self.logged_in

	def login(self):
		self.logged_in = True

	def logout(self):
		username = None
		fname = None
		sname = None
		email = None
		self.logged_in = False

user_l = User_login()

@app.route('/')
def index():
	return render_template('home.html', user_login = user_l.is_login())

@app.route('/home')
def home():
	return render_template('home.html', user_login = user_l.is_login())
	
@app.route('/orphan_homes')
def orphan_homes():
	return render_template('orphan_homes.html', user_login = user_l.is_login())
		
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
	return render_template('about.html', user_login = user_l.is_login())
	
@app.route('/donators')
def donate():
	return render_template('donators.html', user_login = user_l.is_login())

@app.route('/online')
def online():
	return render_template('online.html', user_login = user_l.is_login())

	
@app.route('/contacts')
def contacts():
	return render_template('contacts.html', user_login = user_l.is_login())

@app.route('/user', methods = ['POST', 'GET'])
def user():
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
   				user_l.login()
   				user_l.username = us
   				user_l.fname = fn
   				user_l.sname = sn
   				user_l.email = em
   		except:
   			con.rollback()
   		finally:
   			con.close()
   			return render_template('user.html')


@app.route('/loggedin', methods = ['POST', 'GET'])
def loggedin():
	if request.method == 'POST':
		msga = "initial msg"
		try:
			us = request.form['username']
			ps = request.form['password']

			with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("select fname, sname, email, username from user WHERE username = ? AND password = ?", (us, ps))
				con.commit()
				user = cur.fetchone()
				if(user == None):
					raise Exception()
				else:
					user_l.login()
					user_l.username = user[3]
					user_l.fname = user[0]
	   				user_l.sname = user[1]
	   				user_l.email = user[2]
					msga = us 
		except :
			con.rollback()
		finally:
			con.close()
			if(msga == us):
				return render_template('loggedin.html', msg = msga)
			else:
				return render_template('exists.html')

@app.route('/logout')
def logout():
	user_l.logout()
	return render_template('home.html')

@app.route('/myprofile')
def myprofile():
	return render_template('myprofile.html', username = user_l.username,
												fname = user_l.fname,
												sname = user_l.sname,
												email = user_l.email)

if __name__ == '__main__':
   app.run()
