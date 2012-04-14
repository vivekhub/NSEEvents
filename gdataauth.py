#!/usr/bin/python

import gdata.gauth

def GetAuthSubUrl():
  next = 'http://www.example.com/myapp.py'
  scopes = ['https://www.google.com/calendar/feeds/']
  secure = False  # set secure=True to request a secure AuthSub token
  session = True
  return gdata.gauth.generate_auth_sub_url(next, scopes, secure=secure, session=session)

print '<a href="%s">Login to your Google account</a>' % GetAuthSubUrl()
