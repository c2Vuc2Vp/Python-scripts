#!/usr/bin/python
#-*-coding:utf-8-*-

"""cryptage César revisité"""
"""le decalage va dependre de la longueur du message saisie"""

	

def CCesar(saisie):
	decalage=len(saisie)
	texte_crypter=""
	for x in saisie:
		if (x.islower()):
			texte_crypter += chr((ord(x)-ord(' ')-decalage)%95+ord(' '))
		elif (x.isupper()):
			texte_crypter += chr((ord(x)-ord(' ')-decalage)%95+ord(' '))
		else:
			texte_crypter += x
	return texte_crypter

def DCesar(saisi):
	decalage=len(saisi)
	texte_decrypter=""
	for x in saisi:
		if (x.islower()):
			texte_decrypter += chr((ord(x)-ord(' ')+decalage)%95+ord(' '))
		elif (x.isupper()):
			texte_decrypter += chr((ord(x)-ord(' ')+decalage)%95+ord(' '))
		else:
			texte_decrypter += x
	return texte_decrypter

saisie = str(raw_input("saisi ton msg a crypter la: "))
print CCesar(saisie)
saisi = str(raw_input("saisi ton msg a decrypter la: "))
print DCesar(saisi)
