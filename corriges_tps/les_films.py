continuer = 'o'
# On créé une liste de films vide qui va contenir les films ajoutés
liste_de_films = []
while continuer == 'o':
	# On récupère le nom du film à ajouter
	film_a_ajouter = input('Entrez un titre de film a ajouter: ')
	if film_a_ajouter in liste_de_films:
		print("le film est déjà présent dans la liste")
	else:
		liste_de_films.append(film_a_ajouter)
	# On demande si l'utilisateur veut ajouter un autre film
	continuer = input('Voulez-vous ajouter un autre film? o/n ')
liste_de_films.sort()
print(liste_de_films)