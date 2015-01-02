import os 
import sqlite3

all_rows = []
endl = '\n'

def terminal():
	global all_rows
	directory = os.path.dirname(__file__)
	db = os.path.join(directory, 'db.sqlite3')
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute('SELECT last_login, email, username, first_name, last_name, school_name, student_id FROM {tn}'.format(tn = 'userauth_student'))
	all_rows = c.fetchall()
	#print all_rows
	conn.commit()
	conn.close()
def output():
	data = all_rows
	file = open('database_dump.txt', 'w')
	for x in data:
		empty = []
		for y in x:
			empty.append(str(y))
		file.write(str(empty)+endl)
		file.write('+++++++++++++++Next_Student++++++++++++++++'+endl)

terminal()
output()