#blog.py - controller

from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g
import sqlite3
from functools import wraps

#configuration stuff 
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)

#pull in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)
#function to connect to database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

#function to make sure you're logged in 
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

#making some routes!
#home page
@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or \
			request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error=error)
#after you have logged in
@app.route('/main')
@login_required
def main():
	#connects to the database
	g.db = connect_db()
	#fetches data from the posts table in the database
	cur = g.db.execute('select * from posts')
	#assigns what I just fetched to a dictionary to use later
	posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
	g.db.close()
	#post = post passes the variable to the main.html file
	return render_template('main.html', posts=posts)
#logout
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('login'))


if __name__ == '__main__':
	app.run(debug=True) 