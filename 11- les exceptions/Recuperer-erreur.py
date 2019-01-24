numerateur = 10
denominateur = 'bonjour'

try:
	resultat = numerateur / denominateur
	print(resultat)
except ZeroDivisionError:
	print('Division par zero impossible')
except TypeError:
	print('Une des deux variable nest pas un nombre')

		
