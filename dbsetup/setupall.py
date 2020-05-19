#!/usr/bin/python

# Standard Library
import sys
import sqlite3 as lite

try:
	con = lite.connect('nseann.db')

	with con:
		cur = con.cursor() 
		cur.execute("DROP TABLE IF EXISTS NSEEvents")
		cur.execute("CREATE TABLE NSEEvents(UniqueKey TEXT UNIQUE, ScriptName TEXT NOT NULL, Description TEXT,Value NUMBER,EventDate DATE NOT NULL,CreateDate DATE DEFAULT CURRENT_DATE,Uploaded BOOLEAN, PRIMARY KEY (ScriptName, Description, EventDate))")

except lite.Error as e:
    print("Error %s:" % e.args[0])
