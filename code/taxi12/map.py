#!/usr/bin/python

import sys

count = 0;
countHours = 0
days_data_2015 = ['Thursday','Friday','Saturday','Sunday','Monday','Tuesday','Wednesday'];

for line in sys.stdin:
    data = line.strip().split(",")

    if len(data) != 18:
	continue

    print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],days_data_2015[count]);
    countHours = (countHours+1)%24;
    if countHours == 0: 
        count = (count+1)%7;

