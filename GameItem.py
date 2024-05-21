import sqlite3 as sql

con = sql.connect("itemRef.db")

curr = con.cursor()

curr.execute("CREATE TABLE weapons(name, type, damage)")