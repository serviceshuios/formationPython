age = input("veuillez saisir votre age :")
age = int(age)
if age < 18:
	print("personne mineure")
elif age == 18:
	print("personne à l'age de la majorité")
else:
	print("personne majeure")