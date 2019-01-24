import os
def creer_dossier(structure):
	os.makedirs(structure)
	print("arborescence ", structure," créée")

creer_dossier('C:\\Users\\stagiaire ACI\\Desktop\\StructureSimple')