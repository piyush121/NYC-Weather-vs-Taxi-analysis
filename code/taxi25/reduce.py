#!/usr/bin/python

import sys

oldKey = None

sumTotalTrips = 0
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    thisKey, thisSum = data;
   
    if oldKey and oldKey != thisKey:
	print '%s,%i'%(oldKey,sumTotalTrips);        

        oldKey = thisKey;
        sumTotalTrips = 0

    oldKey = thisKey
    sumTotalTrips += int(1)

if oldKey != None:
    print '%s,%i'%(oldKey,sumTotalTrips);

