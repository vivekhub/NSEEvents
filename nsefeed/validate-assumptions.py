#!/usr/bin/env python

import feedparser
import pprint

thingsaregood = True
d=feedparser.parse('http://feeds.feedburner.com/nseindia/ca')

if 'entries' not in d:
    print 'expecting <entries> in the feed that we didnt find it.'
    thingsaregood = False

items = 0
updatedfound = 0
linkfound = 0

for item in d['entries']:
    items +=1
    
    if 'updated' in item:
        updatedfound +=1

    if 'link' in item:
        linkfound += 1

if updatedfound != items:
    thingsaregood = False
    print 'Out of :' + str(items) + ' items didnt find <updated> field in :' + str(items - updatedfound)

if linkfound != items:
    thingsaregood = False
    print 'Out of :' + str(items) + ' items didnt find <updated> field in :' + str(items - linkfound)

if thingsaregood == False:
    print 'Our assumptions are not valid anymore.  something is broken'
else:
    print 'Our assumption is still good'
