#creating a database for blog app
import sqlite3

#create a new database if the database isn't alreay there
with sqlite3.connect("blog.db") as connection:

	#create the object cursor
	c = connection.cursor()

	#create the table
	c.execute("""CREATE TABLE posts
		(title TEXT, post TEXT)
		""")
	#table should have the columns title and post, all in a text format

	#inserting test data just to make sure everything is set up ok
	c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
	c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
	c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')