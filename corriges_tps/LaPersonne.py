class LaPersonne:
	# attributs de classe
	nb_personnes = 0
	# fonction d'initialisation (constructeur). On va initialiser les attributs
	def __init__(self,nom,prenom,age):
		self.id=0
		self.nom=nom
		self.prenom=prenom
		self.age=age
		self._residence="lille"
		LaPersonne.nb_personnes+=1

	#proprietes
	def _get_residence(self):
		return self._residence

	def _set_residence(self, nouvelle_residence):
		self._residence = nouvelle_residence

	residence = property(_get_residence, _set_residence)

	#méthodes (fonctions)
	
	#méthode classique
	def direBonjour(self):
		return "Bonjour tout le monde je suis une personne"

	#fonction de surcharge d'affichage (__str__)
	def __str__(self):
		"""Méthode permettant d'afficher plus joliment notre objet"""
		return "{0} {1} {2}, âgé de {3} ans habite à {4}".format(self.id,self.prenom, self.nom, self.age,self.residence)

class Employe(LaPersonne):
	#le constructeur de la classe fille dépend de celui de la classe mère
	def __init__(self,nom,prenom,age,salaire):
		super(Employe, self).__init__(nom,prenom,age)
		self.salaire=salaire
		#self.nom=nom
		#self.prenom=prenom
		#self.age=age

	#méthode surchargée
	def direBonjour(self):
		return "Bonjour tout le monde je suis un employé"

paul=LaPersonne("zec","union",12)
print(paul.id,paul.nom,paul.prenom,paul.age,paul.residence)
paul.id=23
print(paul.id,paul.nom,paul.prenom,paul.age,paul._residence)
paul._residence="Paris"
print(paul.id,paul.nom,paul.prenom,paul.age,paul._residence)
paul.lieu_residence="Toulouse"
print(paul.id,paul.nom,paul.prenom,paul.age,paul.lieu_residence)
print(paul.direBonjour())
print(paul)
pierre=Employe("pierre","Dupont",25,2500)
print(pierre)
print(pierre.direBonjour())
print("nombre de personnes créées =",LaPersonne.nb_personnes)
#polymorphisme
print(isinstance(paul, LaPersonne))
print(isinstance(paul, Employe))
print(isinstance(pierre, LaPersonne))
print(isinstance(pierre, Employe))
#Test d'héritage
print(issubclass(LaPersonne, Employe))
print(issubclass(Employe,LaPersonne))