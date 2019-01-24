numerateur = 10
denominateur = 'toto'

# On peut utiliser plusieurs except et specifier l'erreur concernee pour chaque bloc except.
try:
	resultat = numerateur / denominateur
	print(resultat)
except ZeroDivisionError:
	print('Division par zero impossible')
except TypeError:
	print('Une des deux variable nest pas un nombre')
except NameError:
	print('Une variable na pas ete declaree')
