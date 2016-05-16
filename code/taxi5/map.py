#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(",")
    
    if len(data) != 18:
	continue

    data1 =  data[0].strip().split(" ");
    if len(data1)!=2:
        continue
    print '%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s'%(data1[1],data[1],data[3],data[5],data[7],data[9],data[11],data[13],data[15],data[17]);
