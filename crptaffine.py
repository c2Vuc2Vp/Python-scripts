# -*- coding: Latin-1 -*-
#!/usr/bin/env python

####################################
#  Chiffrement par fonction affine #
####################################
import random
 
def tirage_aleatoire(k):
    k=random.randint(1,25)    
    return k

def prepare(PhraseEnClair):
    li1=["âà","éèêë","îï","ô","ûü","ç"]
    li2=["A","E","I","O","U","C"]
    i=0
    # Remplacement des caractères accentués éventuels
    for mot in li1:
       repl=li2[i]
       for lettre in mot:
           PhraseEnClair=PhraseEnClair.replace(lettre,repl)
       i+=1      
    PhraseEnClair=PhraseEnClair.upper()    # Passage en majuscules
    return PhraseEnClair

PhraseEnClair=raw_input("teste de cryptage affine: ")
Acrypter=PhraseEnClair
PhraseEnClair=prepare(PhraseEnClair)
lg=len(PhraseEnClair)

# Tirage aléatoire de la Clé avec a et b différents
k=0
k=tirage_aleatoire(k)
a=k
while k==a:
    k=tirage_aleatoire(k)
b=k
a,b=21,13
# Debut du chiffrement
def CAffine(self):
	MessageCrypte=""
	for i in range(lg):
	    lettre = PhraseEnClair[i]
	    if lettre in " ',-;:!?.":
		MessageCrypte += lettre
	    else:
		MessageCrypte += chr((a*(ord(lettre)-65)+ b)%26 + 65)
	   
	# Affichage du résultat
	print
	print
	print 'Clé : ('+ str(a) + ' ; '+ str(b)+')'
	print "Message d'origine : "+Acrypter
	print "Message codé : "+MessageCrypte
CAffine(PhraseEnClair)
