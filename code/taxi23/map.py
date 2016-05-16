#!/usr/bin/python

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split(",")

    if len(data) != 19:
	continue

    data1 = data[1].strip().split(" ");
    data2 = data1[1].strip().split(":")

    pickup_time = datetime.strptime(data[1],'%Y-%m-%d %H:%M:%S')
    dropoff_time = datetime.strptime(data[2],'%Y-%m-%d %H:%M:%S')


    duration = dropoff_time-pickup_time
    duration_minutes = str(duration).strip().split(":")

    h = int(duration_minutes[0]);
    m = int(duration_minutes[1]);
    s = int(duration_minutes[2]);
    #print h,' - ',m,'-',s
    duration_minute =  60*h + m
    #print duration_minute
    if len(data1)!=2 and len(data2)!=3:
        continue
    print '%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s'%(data2[0],data[3],data[4],data[12],data[13],data[14],data[15],data[16],data[18],duration_minute);
