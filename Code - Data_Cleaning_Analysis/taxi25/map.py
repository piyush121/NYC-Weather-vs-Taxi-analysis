#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(",")

    if len(data) != 19:
	continue

    data1 = data[1].strip().split(" ");
    data2 = data1[1].strip().split(":");

    if len(data1)!=2 and len(data2)!=3:
        continue
    print '%s\t%i'%(data2[0],int(1));
