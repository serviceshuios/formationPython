chemin ='C:\\Users\\stagiaire ACI\\Desktop\\Christian.txt'

f = open(chemin, 'r')

# Pour récupérer le contenu complet du fichier dans une chaine de caractère
#f.read()

# Pour récupérer une liste qui contient chaque ligne
#f.readlines()

# Pour boucler à travers chaque ligne
# Avec une boucle For
for line in f.readlines():
	print(line)

# Avec une boucle While
#line = f.readline()
#while line:
#	print(line)
#	line = f.readline()
