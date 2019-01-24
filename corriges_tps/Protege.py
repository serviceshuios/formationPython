class Protege:
	"""Classe possédant une méthode particulière d'accès à ses attributs :
	Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None"""
	def __init__(self):
		"""On crée quelques attributs par défaut"""
		self.a = 1
		self.b = 2
		self.c = 3

	def __getattr__(self, nom):
		"""Si Python ne trouve pas l'attribut nommé nom, il appelle cette méthode."""
		print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

	def __setattr__(self, nom_attr, val_attr):
		"""Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet"""
		object.__setattr__(self, nom_attr, val_attr)

	def __delattr__(self, nom_attr):
		"""On ne peut supprimer d'attribut, on lève l'exception
        AttributeError"""
		raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")