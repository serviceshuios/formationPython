continuer = 'o'

while continuer == 'o':

	nombre = input('Entrez un nombre: ')

	for i in range(1, 11):
		print('{0} x {1} = {2}'.format(i, nombre, int(nombre) * i))

	continuer = input('Voulez-vous continuer? o/n ')

print('Fin du script.')
