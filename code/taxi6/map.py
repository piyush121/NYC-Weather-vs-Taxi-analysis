#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(",");

    if len(data) == 19 and data[11]!='payment_type' and int(data[11])==2:
	data1 = data[1].strip().split(" ")
	print "%s\t%i"%(data1[0],int(1));
