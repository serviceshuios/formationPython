import os

def creer_dossiers(structure):
    for key, values in structure.items():
        for value in values:
            dossier = '{0}/{1}/{2}'.format(base, key, value)
            print('Creation du dossier {0}'.format(dossier))
            os.makedirs(dossier)

base = 'C:\\Users\\stagiaire ACI\\Desktop\\Structure'
base = base.replace('\\', '/')

structure = {
             'Musique': ['Rock', 'Jazz', 'Pop'],
             'Documents': ['Factures', 'Travail', 'Maison'],
             'Images': ['Vacances', 'Famille'],
             'Videos': ['Concert', 'Chat', 'Facebook']
            }

creer_dossiers(structure)






