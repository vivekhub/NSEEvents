#!/usr/bin/python

import parsefeed
import savedb


def main():
  fi = parsefeed.loadparsefeed()
  print 'Found ' ,  len(fi), 'items'
  savedcount = savedb.savedb(fi)
  print 'Added ', savedcount , ' items to the database'

  
  
if __name__ == '__main__':
	main()
