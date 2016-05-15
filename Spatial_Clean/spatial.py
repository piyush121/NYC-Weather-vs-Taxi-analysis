from rtree import index

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


def simplePolygonTest():
	print("Point in polygon test")
	# Create a simple polygon
	poly = Polygon([Point(0.0, 0.0),Point(0.0, 4.0),Point(3.0, 4.0),Point(3.0, 0.0)])
	
	# Create two points
	pt1 = Point(1,1)
	pt2 = Point(3,3)

	# Test if the polygon contains the two points
	if poly.contains(pt1):
		print("Point 1 is within the polygon")
	else:
		print("Point 1 is outside the polygon")
	if poly.contains(pt2):
		print("Point 2 is within the polygon")
	else:
		print("Point 2 is outside the polygon")


def simpleRTree():
	print("R-tree test")
	poly = Polygon([Point(0.0, 0.0),Point(0.0, 4.0),Point(3.0, 4.0),Point(3.0, 0.0)])
	idx = index.Index()
	pt1 = Point(1,1)
	pt2 = Point(4,1)
	pt3 = Point(3,3)
	# Insert the points into the R-tree index
	idx.insert(1,(pt1.x,pt1.y,pt1.x,pt1.y))
	idx.insert(2,(pt2.x,pt2.y,pt2.x,pt2.y))
	idx.insert(3,(pt3.x,pt3.y,pt3.x,pt3.y))

	# Query. This library only supports rectangular queries

	# Specify the bounds
	leftBottom = Point(0,0)
	rightTop = Point(3,4)

	# Perform the query
	results = list(idx.intersection((leftBottom.x,leftBottom.y,rightTop.x,rightTop.y), objects=True))
	print("Query result:")
	cnt=0
	for res in results:
		pt = Point(res.bbox[0],res.bbox[1])
		if poly.contains(pt):
			cnt = cnt + 1
	print str(cnt)
simplePolygonTest()
simpleRTree()
