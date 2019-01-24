def filtre(source,destination):
	"recopier un fichier en éliminant les lignes de remarques"
	fs = open(source, 'r')
	fd = open(destination, 'w')
	while 1:
		txt = fs.readline()
		if txt =='':
			break
		if '#' not in txt:
			fd.write(txt)
	fs.close()
	fd.close()
	#return

filtre("les_films.py","les_films_sans_commentaires.py")