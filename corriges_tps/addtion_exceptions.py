def addition(a,b):
	c=0
	try:
		c=a/b
	except:
		print("il y a une erreur dans l'opération")
	finally:
		return c

print(addition(15,2))
print(addition(15,0))