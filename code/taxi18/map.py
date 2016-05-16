#!/usr/bin/python

import sys

count = 1 
for line in sys.stdin:
    data = line.strip().split(",")

    if len(data) != 20 or ("SevereSnow" not in line) or count == 1:
	count = 0 ;
	continue
    data1 = data[0].strip().split(" ")

    print '%s %s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(str(data[18]),str(data1[1]),str(data[1]),str(data[2]),str(data[3]),str(data[4]),str(data[5]),str(data[6]),str(data[7]),str(data[8]),str(data[9]),str(data[10]),str(data[11]),str(data[12]),str(data[13]),str(data[14]),str(data[15]),str(data[16]),str(data[17]));

