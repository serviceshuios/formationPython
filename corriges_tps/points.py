#déclaration de la fonction initialisation
def init(x=0,y=0):
	x=1
	y=1
#init(4,5)

#déplacement
def deplacement(x,y,dx,dy):
	x+=dy
	y+=dy
	return (x,y)
# affichage
def affichage(x,y):
	#init(x,y)
	print([x,y])

affichage(4,5)
(a,b)=deplacement(4,5,1,1)
affichage(a,b)