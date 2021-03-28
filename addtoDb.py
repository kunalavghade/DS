import sqlite3

conn=sqlite3.connect("database.db")
cor=conn.cursor()

conn.execute('''CREATE TABLE "Food" (
			"No"	INTEGER PRIMARY KEY AUTOINCREMENT,
			"Name"	TEXT,
			"Rs"	INTEGER,
			"Type"	TEXT 
		);''')
conn.commit()

with open("Hotel manue.txt") as file:
	line = file.readlines()
	for x in line:
		y=x.split("+")
		try:
			print(y[1],y[3],y[5])
			cor.execute("insert into 'Food' (Name,Rs,Type) values(?,?,?)",(y[1],int(y[3]),y[5]))
			conn.commit()
		except :
			pass

