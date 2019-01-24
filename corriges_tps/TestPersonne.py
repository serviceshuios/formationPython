from Personne import *
from Protege import *

jean = Personne("Micado", "Jean")
pierre = Personne("Micado", "Pierre")
print(jean.nom)
print(jean.prenom)
print(jean.age)
print(jean.lieu_residence)
jean.lieu_residence = "Berlin"
print(jean.lieu_residence)

print("nombre de personnes = ",Personne.nb_personnes)
print(jean)
pro = Protege()
print(pro.a)
print(pro.c)
print(pro.e)

