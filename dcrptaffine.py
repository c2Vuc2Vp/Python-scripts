# -*- coding: Latin-1 -*-
#!/usr/bin/env python

##################################################
#  Décodage d'un chiffrement par fonction affine #
##################################################
saisie=raw_input("teste de décrypage: ").upper()
def DAffine (self):
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
	print
	print
	print 'Avec L --> K  et  E --> T, la Clé est : ('+ str(a) + ' ; '+ str(b)+')'
	print
	print "Message d'origine : "+saisie
	print
	print "Message clair     : "+MessageClair
DAffine(saisie)
