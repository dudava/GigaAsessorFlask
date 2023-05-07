import sqlite3

con = sqlite3.connect('db/users.db')

with con:
	con.execute("""CREATE TABLE IF NOT EXISTS User (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		login TEXT
	)""")


sql = 'INSERT INTO User (login) values (?)'
data = [
	('dudavik')
]
with con:
	con.execute(sql, data)

with con:
	data = con.execute('SELECT * FROM User')
	for row in data:
		print(row)