chemin ='C:\\Users\\stagiaire ACI\\Desktop\\Christian.txt'

# Pour écrire dans un fichier et écraser son contenu
#f = open(chemin, 'w')
#f.write('encore du Nouveau contenu')
#f.close()

# Pour écrire dans un fichier et rajouter du contenu à sa suite
f = open(chemin, 'a')
f.write('\nContenu ajouté')
f.close()
