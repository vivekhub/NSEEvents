#/usr/bin/python
"""
    Simple robust time and date parsing.
    
    Note: Follows the Australian standard, dd/mm/yyyy.
          Americans should replace '%d %m %Y' with '%m %d %Y' and '%d %m %y' with '%m %d %y' below.
    
    Routines will either
     - return a date or time
     - return None if the string is empty
     - throw a ValueError
     
    TODO: Handle 1st 2nd 3rd etc

    This file is placed in the public domain by Paul Harrison, 2006
"""

__version__ = '0.1'

# Standard Library
import time
import datetime

time_formats = ['%H : %M', '%I : %M %p', '%H', '%I %p']

date_formats_with_year = ['%d %m %Y', '%Y %m %d', '%d %B %Y', '%B %d %Y',
                                                  '%d %b %Y', '%b %d %Y',
                          '%d %m %y', '%y %m %d', '%d %B %y', '%B %d %y',
                                                  '%d %b %y', '%b %d %y']

date_formats_without_year = ['%d %B', '%B %d',
                             '%d %b', '%b %d']

def parse_time(string):
    string = string.strip()
    if not string: return None
    
    for format in time_formats:
        try:
            result = time.strptime(string, format)
            return datetime.time(result.tm_hour, result.tm_min)
        except ValueError:
            pass
            
    raise ValueError()

    
def parse_date(string):
    string = string.strip()
    if not string: return None
    
    string = string.replace('/',' ').replace('-',' ').replace(',',' ')
    
    for format in date_formats_with_year:
        try:
            result = time.strptime(string, format)
            return datetime.date(result.tm_year, result.tm_mon, result.tm_mday)
        except ValueError:
            pass

    for format in date_formats_without_year:
        try:
            result = time.strptime(string, format)
            year = datetime.date.today().year
            return datetime.date(year, result.tm_mon, result.tm_mday)
        except ValueError:
            pass
            
    raise ValueError()


if __name__ == '__main__':
    # Run some simple tests
    for test in ['1pm', '13:30', '5:05pm']:
        print(parse_time(test), test)

    for test in ['2/6/1977', '02/06/77', '1977-06-02', '2 June, 1977', 'Jun 2, 1977', '2 June', 'Jun 2']:
        print(parse_date(test), test)
