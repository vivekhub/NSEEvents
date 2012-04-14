#!/usr/bin/python

import sqlite3 as lite
import sys

try:
	con = lite.connect('nseann.db')

	with con:
		cur = con.cursor() 
		cur.execute("DROP TABLE IF EXISTS NSEEvents")
		cur.execute("CREATE TABLE NSEEvents(UniqueKey TEXT UNIQUE, ScriptName TEXT NOT NULL, Description TEXT,EventDate DATE NOT NULL, Uploaded BOOLEAN, PRIMARY KEY (ScriptName, Description, EventDate))")

except lite.Error, e:
    print "Error %s:" % e.args[0]
