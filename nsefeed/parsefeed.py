#!/usr/bin/python

import feedparser
import hashlib 
import parse_datetime as pdt
from pprint import pprint

import sqlite3 as lite
import sys

def loadparsefeed():
    feeditems=[]
    d=feedparser.parse('http://feeds.feedburner.com/nseindia/ca')
    for item in d['entries']:
      parseditem = parseNSEitem(item)
      feeditems.append(parseditem)
    return feeditems

def parseNSEitem(item):
    m = hashlib.md5()
    timeslot = None

    timeslot = item.get('published')

    if timeslot is None:
        timeslot = item.get('updated')

    m.update(item['link'] + timeslot)
    myguid = m.hexdigest()
    #The assumption here is that the title contains the format 'blah blah blah company - Ex-Date: <date>
    titleitems = item['title'].split('- Ex-Date:')
    summaryitems = item['summary'].split('<div')
        

    return (myguid, titleitems[0], summaryitems[0],pdt.parse_date(titleitems[1]),False)

if __name__ == '__main__':
    f = loadparsefeed()
    pprint(f)
