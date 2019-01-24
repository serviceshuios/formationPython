import os
def creer_dossier(structure,sousReps):
	for rep in sousReps:
		os.makedirs(structure+'/'+rep)
		print("arborescence ", structure+"/"+rep, "créée")

creer_dossier('C:/Users/stagiaire ACI/Desktop/StructureComplexe',['images','videos','photos'])