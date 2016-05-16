#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(",");

    if len(data) == 19 and data[3]!='passenger_count':
	if int(data[3]) == 0:
	    print "%s\t%i"%('a',int(1));
        elif int(data[3]) == 1:
            print "%s\t%i"%('b',int(1));
        elif int(data[3]) == 2:
            print "%s\t%i"%('c',int(1));
        elif int(data[3]) == 3:
            print "%s\t%i"%('d',int(1));
        elif int(data[3]) == 4:
            print "%s\t%i"%('e',int(1));
        elif int(data[3]) == 5:
            print "%s\t%i"%('f',int(1));
        elif int(data[3]) == 6:
            print "%s\t%i"%('g',int(1));
        elif int(data[3]) == 7:
            print "%s\t%i"%('h',int(1));
        else:
            print "%s\t%i"%('i',int(1));

