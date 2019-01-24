personne = {'id':1,'nom':'zec','prenom':'union','age':20}
# affichage du dictionnaire
print(personne)
#afficher la valeur de la clé nom
print(personne['nom'])
#ajouter la clé genre avec pour valeur 'M'
personne['genre']='M'
print(personne)
#afficher toutes les clés
for cle in personne.keys():
	print(cle)

#afficher toutes les valeurs 
for valeurs in personne.values():
	print(valeurs)

#créer une copie du dictionnaire
personne2=personne.copy()
print(personne)
print(personne2)

# supprimer la clé genre dans personne2
personne2.pop('genre')
print(personne)
print(personne2)

# tester si la clé nom appartient a personne
if 'nom' in personne.keys():
	print("nom est une clé du dictionnaire personne")
else:
	print("nom n'est pas une clé du dictionnaire personne")

#print(personne.has_key('nom'))
if 5 in personne.values():
	print(5," est une valeur du dictionnaire")
else:
	print(5," n'est pas une valeur du dictionnaire")