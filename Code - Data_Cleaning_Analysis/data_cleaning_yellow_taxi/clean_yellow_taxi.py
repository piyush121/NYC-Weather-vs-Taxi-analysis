#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(",");

    try:
        if len(data) != 19:
	    continue;
        if data[0]=='VendorId':
	    continue;
		if len(data[1].strip().split(" ")) != 2 or len(data[1].strip().split(":"))!=3 or len(data[2].strip().split(" ")) != 2 or len(data[2].strip().split(":")) != 3 :
			continue
		if int(data[3]) < 0:
			continue
		if float(data[4]) < 0.0 or float(data[4]) > 1000.0:
			continue
		if int(data[7]) not in range(1,7):
			continue
		if data[8] not in ['Y','N']:
			continue
		if int(data[11]) not in range(1,7):
			continue
		if float(data[12]) < 0.0:
			continue
		if float(data[14]) not in [0.0,0.5]:
			continue
		if float(data[15]) < 0.0 or float(data[15])> 1000.0:
			continue
		if int(data[16]) < 0:
			continue
		if float(data[17]) not in [0,0,0.30]:
			continue
		if float(data[18]) < 0.0:    
			continue
		print line
		except ValueError:
			continue        
