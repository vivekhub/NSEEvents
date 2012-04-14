#!/usr/bin/python

import sqlite3 as lite
import sys
import datetime

def savedb(feeditems):
	try:
		con = lite.connect('nseann.db')
		with con:
			cur = con.cursor()    
			cur.executemany('INSERT OR IGNORE INTO NSEEvents VALUES( ?, ?, ?, ?, ?)', feeditems)
			rval = cur.rowcount
		con.commit()
		return rval
	
	except lite.Error, e:
		print "Error %s:" % e.args[0]


if __name__ == '__main__':
	testval = [('2c00978681a672e22f11fb579803f902', u'Blue Dart Express Limited', 
	  u'ANNUAL GENERAL MEETING AND DIVIDEND RS.2/- PER SHARE',
	datetime.date(2012, 4, 13), False), ('2c00978681a672e22f11fb5798034334',
	  u'Blue Dart Express Limited ', 
	  u'ANNUAL GENERAL MEETING AND DIVIDEND RS.2/- PER SHARE', datetime.date(2012, 4, 13), False)]

	print savedb(testval)
