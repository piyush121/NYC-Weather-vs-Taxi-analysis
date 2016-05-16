#!/usr/bin/python

import sys

oldKey = None
totalSum = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    thisKey, thisValue = data; 

    if oldKey and oldKey != thisKey:
	print "%s,%i"%(oldKey,totalSum)
        oldKey = thisKey;
	totalSum = 0

    oldKey = thisKey;
    totalSum += int(1)

if oldKey != None:
    print "%s,%i"%(oldKey,totalSum)

