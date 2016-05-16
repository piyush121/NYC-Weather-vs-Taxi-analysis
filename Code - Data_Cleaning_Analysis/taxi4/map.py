#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(",")

    if len(data) != 19:
	continue

    print '%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(data[18],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17]);

