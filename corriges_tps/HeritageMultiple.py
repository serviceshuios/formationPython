class Mere1:
	attribut = "mere1 attribut"

class Mere2:
	attribut = "mere2 attribut"

class Fille1(Mere1,Mere2):
	def methode(self):
		print(self.attribut)

class Fille2(Mere2,Mere1):
	def methode(self):
		print(self.attribut)

m1 = Mere1()
m1.attribut

m2 = Mere2()
m2.attribut

f1 = Fille1()
f1.methode()

f2 = Fille2()
f2.methode()