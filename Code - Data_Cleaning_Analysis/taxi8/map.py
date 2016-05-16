#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(",");

    if len(data) == 19 and data[4]!='trip_distance':
	if float(data[4]) < 1.0:
	    print "%s\t%i"%('a',int(1));
        elif float(data[4]) < 2.0:
            print "%s\t%i"%('b',int(1));
        elif float(data[4]) < 3.0:
            print "%s\t%i"%('c',int(1));
        elif float(data[4]) < 5.0:
            print "%s\t%i"%('d',int(1));
        elif float(data[4]) < 10.0:
            print "%s\t%i"%('e',int(1));
        elif float(data[4]) < 20.0:
            print "%s\t%i"%('f',int(1));
        elif float(data[4]) < 50.0:
            print "%s\t%i"%('g',int(1));
        else:
            print "%s\t%i"%('h',int(1));


