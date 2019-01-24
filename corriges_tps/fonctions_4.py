def carre(a):
	c=a*a
	return c

def testDivision(a):
	resultat = False
	if a%10==0 and a%3!=0:
		resultat = True
	else:
		resultat = False
	return resultat

def calculVoyelles(chaine):
	voyelles = ['a','e','i','o','u','y']
	nombre=0
	for lettre in chaine:
		if lettre in voyelles:
			nombre+=1
	return nombre

def factorielle(x):
	resultat = 1
	if x!=0 and x!=1:
		resultat=x*factorielle(x-1)
	return resultat

x=carre(4)
print(x)

y=testDivision(15)
print(y)

z=calculVoyelles('bonjour')
print(z)

a=factorielle(3)
print(a)
