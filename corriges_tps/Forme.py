class Forme:
	point_origine
	def __init__ (self) :
		self.point_origine.x=0
		self.point_origine.y=0
	def calculerDistance(self,point):
		distanceX=self.point_origine.x-point.x
		distanceY = self.point_origine.y - point.y
		return sqrt(distanceX**2+distanceY**2)

	def calculerPerimetre(self):

	def afficher(self):
		print(self.point_origine.x," ",self.point_origine.y)

class Rectangle(Point)

class Cercle(Point)