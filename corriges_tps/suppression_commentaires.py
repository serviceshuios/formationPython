def filtre(source,destination):
	"recopier un fichier en éliminant les lignes de remarques"
	try:
		fs = open(source, 'r')
		fd = open(destination, 'w')
		while 1:
			txt = fs.readline()
			if txt =='':
				break
			if txt[0] != '#':
				fd.write(txt)
		fs.close()
		fd.close()
	except FileNotFoundError:
		print("fichier source introuvable")
	#return

filtre("commentaires.txt","sans_commentaires.txt")