class Vehicule :
	def __init__ (self) :
		self.nombreRoues = 4
		self.placesAssises = 2
		self.consomation = 8
	def calculConso (self, distance) :
		return float(self.consomation) * distance / 100


class Autobus (Vehicule) :
	def __init__ (self) :
		self.nombreRoues = 8
		self.placesAssises = 30
		self.consomation = 25

vehic = Vehicule()
bus = Autobus()
print(vehic.calculConso(30))
print(bus.calculConso(30))