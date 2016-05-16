#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(",")

    if len(data) != 19:
	continue

    data1 =  data[1].strip().split(" ");
    if len(data1)!=2:
        continue
    print '%s\t%s,%s,%s,%s,%s,%s,%s,%s'%(data1[0],data[3],data[4],data[12],data[13],data[14],data[15],data[16],data[18]);
