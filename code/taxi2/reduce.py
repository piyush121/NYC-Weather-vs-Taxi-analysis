#!/usr/bin/python

import sys

oldKey = None

sumTotalTrips = 0
sumTotalPassengers = 0
sumTotalTripDistance = 0.0
sumTotalFareAmount = 0.0
sumTotalExtraAmount = 0.0
sumTotalMTATax = 0.0
sumTotalTipAmount = 0.0
sumTotalTollsAmount = 0.0
sumTotalTotalAmount = 0.0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    data1 = data[1].strip().split(",")

    if len(data1) != 8:
	continue

    thisKey, thisSum = data;

    thisPassengers, thisTripDistance, thisFareAmount, thisExtraAmount, thisMTATax, thisTipAmount, thisTollsAmount, thisTotalAmount = data1
   
    if oldKey and oldKey != thisKey:
        print '%s,%i,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%i'%(oldKey,int(sumTotalPassengers),float(float(sumTotalPassengers)/sumTotalTrips),sumTotalTripDistance, float(sumTotalTripDistance/sumTotalTrips), sumTotalFareAmount, float(sumTotalFareAmount/sumTotalTrips),sumTotalExtraAmount, float(sumTotalExtraAmount/sumTotalTrips),sumTotalMTATax, float(sumTotalMTATax/sumTotalTrips),sumTotalTipAmount,float(sumTotalTipAmount/sumTotalTrips),sumTotalTollsAmount,float(sumTotalTollsAmount/sumTotalTrips),sumTotalTotalAmount,float(sumTotalTotalAmount/sumTotalTrips),int(sumTotalTrips))

        oldKey = thisKey;
        sumTotalTrips = 0
	sumTotalPassengers = 0
	sumTotalTripDistance = 0.0
	sumTotalFareAmount = 0.0
	sumTotalExtraAmount = 0.0
	sumTotalMTATax = 0.0
	sumTotalTipAmount = 0.0
	sumTotalTollsAmount = 0.0
	sumTotalTotalAmount = 0.0

    oldKey = thisKey
    sumTotalTrips += int(1)
    sumTotalPassengers += int(thisPassengers)
    sumTotalTripDistance += float(thisTripDistance)
    sumTotalFareAmount += float(thisFareAmount)
    sumTotalExtraAmount += float(thisExtraAmount)
    sumTotalMTATax += float(thisMTATax)
    sumTotalTipAmount += float(thisTipAmount)
    sumTotalTollsAmount += float(thisTollsAmount)
    sumTotalTotalAmount += float(thisTotalAmount)


if oldKey != None:
   print '%s,%i,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%i'%(oldKey,int(sumTotalPassengers),float(float(sumTotalPassengers)/sumTotalTrips),sumTotalTripDistance, float(sumTotalTripDistance/sumTotalTrips), sumTotalFareAmount, float(sumTotalFareAmount/sumTotalTrips),sumTotalExtraAmount, float(sumTotalExtraAmount/sumTotalTrips),sumTotalMTATax, float(sumTotalMTATax/sumTotalTrips),sumTotalTipAmount,float(sumTotalTipAmount/sumTotalTrips),sumTotalTollsAmount,float(sumTotalTollsAmount/sumTotalTrips),sumTotalTotalAmount,float(sumTotalTotalAmount/sumTotalTrips),int(sumTotalTrips))
 
