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
	month = 'jan'
	financial = Polygon([Point(40.712227, -74.017941),Point(40.705998, -74.019370),Point(40.702284, -74.016768),Point(40.700620, -74.013603),Point(40.700975, -74.011141),Point(40.706181, -74.001724),Point(40.712227, -74.017941)])
	nyu = Polygon([Point(40.733585, -73.999545),Point(40.729755, -74.002174),Point(40.726575, -73.995805),Point(40.730597, -73.992469),Point(40.733585, -73.999545)])
	timesquare = Polygon([Point(40.757181, -73.989846),Point(40.754863, -73.984124),Point(40.763706, -73.977803),Point(40.766047, -73.983399),Point(40.757181, -73.989846)])
	brooklyn = Polygon([Point(40.704342, -73.993896),Point(40.697087, -73.998832),Point(40.692076, -73.982610),Point(40.704310, -73.982781),Point(40.704342, -73.993896)])
	jfk = Polygon([Point(40.6188, -73.7712),Point(40.6233, -73.7674),Point(40.6248, -73.7681),Point(40.6281, -73.7657), Point(40.6356, -73.7472), Point(40.6422, -73.7468), Point(40.6469, -73.7534), Point(40.6460, -73.7544), Point(40.6589, -73.7745),Point(40.6628, -73.7858), Point(40.6634, -73.7891), Point(40.6655, -73.7903), Point(40.6658, -73.8021),Point(40.6632, -73.8146),Point(40.6638, -73.8210), Point(40.6621, -73.8244), Point(40.6546, -73.8248), Point(40.6469, -73.8212), Point(40.6302, -73.7848), Point(40.6223, -73.7899),Point(40.6203, -73.7831),Point( 40.6274, -73.7782),Point(40.6235, -73.7731),Point(40.6193, -73.7738),Point(40.6188, -73.7712)])
	count=0
	f1 = open('./data/financialtojfk_'+month+'.csv','w')
	f2 = open('./data/nyutojfk_'+month+'.csv','w')
	f3 = open('./data/timesquaretojfk_'+month+'.csv','w')
	f4 = open('./data/brooklyntojfk_'+month+'.csv','w')
	with open('yellow_tripdata_2015-01.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		skip=0
		start_time=time.time()
		for row in spamreader:
			if(skip<1):
				f1.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+","+row[18]+"\n")
				f2.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+","+row[18]+"\n")
				f3.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+","+row[18]+"\n")
				f4.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+","+row[18]+"\n")
				skip = skip+1
				continue
			lat=float(row[6])
			lon=float(row[5])
			pt=Point(lat,lon)
			lat1=float(row[10])
			lon1=float(row[9])
			pt1=Point(lat1,lon1)
			if jfk.contains(pt1):
				if financial.contains(pt) :
					count=count+1
					f1.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+","+row[18]+"\n")
				elif nyu.contains(pt):
					count=count+1
					f2.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+","+row[18]+"\n")
				elif timesquare.contains(pt):
					count=count+1
					f3.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+","+row[18]+"\n") 
				elif brooklyn.contains(pt):
					count=count+1
					f4.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+","+row[18]+"\n") 
	end_time=time.time()-start_time
	print "Total number of hits is -------------> %d" %(count)
	print "\nTotal time taken = "+str(end_time)
	f1.close()
	f2.close()
	f3.close()
	f4.close()


print "Running on data without indexing..."
taxiJFKTest()
