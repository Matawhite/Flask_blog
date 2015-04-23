#blog.py - controller

from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g
import sqlite3

DATABASE = 'blog.db'

app = Flask(__name__)

#pull in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)
#function to connect to database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
	app.run(debug=True) 