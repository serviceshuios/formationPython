nombre = input("veuillez rentrer un nombre :")
nombre = int(nombre)
for i in range(1,11):
	print("{0} x {1} = {2}".format(i,nombre,i*nombre))