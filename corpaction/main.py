#!/usr/bin/env python

import savedb
import parse_corpaction


def main():
    fi = parse_corpaction.loadparsefeed()
    print('Found ', len(fi), 'items')
    savedcount = savedb.savedb(fi)
    print('Added ', savedcount, ' items to the database')


if __name__ == '__main__':
    main()
