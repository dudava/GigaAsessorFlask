import sqlite3

con = sqlite3.connect('db/users.db', check_same_thread=False)


def db_init():
	with con:
		con.execute("""CREATE TABLE IF NOT EXISTS User (
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			login TEXT
		)""")
