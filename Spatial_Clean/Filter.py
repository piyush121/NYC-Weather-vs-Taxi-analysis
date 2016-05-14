import csv
import StringIO
from rtree import index
import time
import sys

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Polygon:
	def __init__(self,points):
		self.points = points
		self.nvert = len(points)

		minx = maxx = points[0].x
		miny = maxy = points[0].y
		for i in xrange(1,self.nvert):
			minx = min(minx,points[i].x)
			miny = min(miny,points[i].y)
			maxx = max(maxx,points[i].x)
			maxy = max(maxy,points[i].y)

		self.bound = (minx,miny,maxx,maxy)


	def contains(self,pt):
		firstX = self.points[0].x
		firstY = self.points[0].y
		testx = pt.x
		testy = pt.y
		c = False
		j = 0
		i = 1
		nvert = self.nvert
		while (i < nvert) :
			vi = self.points[i]
			vj = self.points[j]
			
			if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
				c = not(c)

			if(vi.x == firstX and vi.y == firstY):
				i = i + 1
				if (i < nvert):
					vi = self.points[i];
					firstX = vi.x;
					firstY = vi.y;
			j = i
			i = i + 1
		return c

	def bounds(self):
		return self.bound


def taxiJFKTest():
	# Create a simple polygon
	myPoly = Polygon([Point(40.711595, -74.015831),Point(40.707441, -74.004136),Point(40.702920, -74.011487),Point(40.706226, -74.017952),Point(40.711595, -74.015831)])
	poly = Polygon([Point(40.6188, -73.7712),Point(40.6233, -73.7674),Point(40.6248, -73.7681),Point(40.6281, -73.7657), Point(40.6356, -73.7472), Point(40.6422, -73.7468), Point(40.6469, -73.7534), Point(40.6460, -73.7544), Point(40.6589, -73.7745),Point(40.6628, -73.7858), Point(40.6634, -73.7891), Point(40.6655, -73.7903), Point(40.6658, -73.8021),Point(40.6632, -73.8146),Point(40.6638, -73.8210), Point(40.6621, -73.8244), Point(40.6546, -73.8248), Point(40.6469, -73.8212), Point(40.6302, -73.7848), Point(40.6223, -73.7899),Point(40.6203, -73.7831),Point( 40.6274, -73.7782),Point(40.6235, -73.7731),Point(40.6193, -73.7738),Point(40.6188, -73.7712)])
	count=0
	f = open('spatial_cleanFinancialDistrict.csv','w')
	with open('yellow_tripdata_2015-01.csv', 'rb') as csvfile:
		#cs=StringIO.StringIO(csvfile)
		spamreader = csv.reader(csvfile, delimiter=',')
		skip=0
		start_time=time.time()
		for row in spamreader:
			if(skip<1):
				f.write(str(row)+"\n")
				skip = skip+1
				continue
			lat=float(row[6])
			lon=float(row[5])
			pt=Point(lat,lon)
			if myPoly.contains(pt):
				count=count+1
				f.write(str(row)+"\n") 
	end_time=time.time()-start_time
	print "Total number of hits is -------------> %d" %(count)
	print "\nTotal time taken = "+str(end_time)
	f.close()


print "Running on data without indexing..."
taxiJFKTest()
