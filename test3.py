#coding=utf-8

import random

def tirage_aleatoire(k):
    k=random.randint(1,25)    
    return k

def prepare(saisie):
    li1=["âà","éèêë","îï","ô","ûü","ç"]
    li2=["A","E","I","O","U","C"]
    i=0
    # Remplacement des caractères accentués éventuels
    for mot in li1:
       repl=li2[i]
       for lettre in mot:
           saisie=saisie.replace(lettre,repl)
       i+=1      
    saisie=saisie.upper()    # Passage en majuscules
    return saisie
    
    

# Tirage aléatoire de la Clé avec a et b différents
k=0
k=tirage_aleatoire(k)
a=k
while k==a:
    k=tirage_aleatoire(k)
b=k
a,b=21,13

def CAffine(self):
	lg=len(saisie)
	MessageCrypte=""
	for i in range(lg):
	    lettre = saisie[i]
	    if lettre in " ',-;:!?.":
		MessageCrypte += lettre
	    else:
		MessageCrypte += chr((a*(ord(lettre)-65)+ b)%26 + 65)
	   
	# Affichage du résultat
	print 'Clé : ('+ str(a) + ' ; '+ str(b)+')'
	return MessageCrypte.capitalize()

def DAffine(self):
	lg=len(saisie)
	MessageClair=""
	# Recherche de la clé sachant que L --> K et  E --> T
	# Affectation des valeurs des lettres : ax+b=y puis axx+b=yy
	x,y = ord('L')-65,ord('K')-65
	xx,yy = ord('E')-65,ord('T')-65

	# Résolution du système
	u,v=xx-x,yy-y
	if u < 0:
	    u,v=x-xx,y-yy
	k=0
	while not ((v+26*k)%u==0 and v+26*k >0):
	    k+= 1
	a = int((v+26*k)/u)

	b=y-a*x
	k=0
	while not y-a*x+26*k > 0:
	    k+= 1
	b = y-a*x+26*k

	# Déchiffrement proprement dit
	for i in range(lg):
	    lettre = saisie[i]
	    if lettre in " ',-;:!?.":
		MessageClair+= lettre
	    else:
		res,k=ord(lettre)-65-b,0
		while (res+26*k)%a>0 or res+26*k<0:
		    k+=1
		MessageClair += chr((res+26*k)/a+65)
	   
	# Affichage du résultat
	# Si tu le souhaite tu peux print ('Avec L --> K  et  E --> T, la Clé est : ('+ str(a) + ' ; '+ str(b)+')')
	return MessageClair.capitalize()
saisie = raw_input("> ")
saisie = prepare(saisie)
print CAffine(saisie)
print DAffine(saisie)
