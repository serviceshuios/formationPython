from math import *
class Point :
	def __init__(self):
		self.x=0
		self.y=0
	def distance(self,):
		distanceX = self.x - point.x
		distanceY = self.y - point.y
		return sqrt(distanceX**2+distanceY**2)
	def deplacer(self,deplX,deplY):
		self.x += deplX
		self.y += deplY