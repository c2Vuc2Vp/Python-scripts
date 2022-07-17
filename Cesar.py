#!/usr/bin/python
#-*-coding:utf-8-*-
"""chiffrement Cesar"""
texte_crypter = ""
class Crpt:
	def Cesar():
		decalage = len(texte_saisie)
		if len(texte_saisie)>25:
			tsaisie = texte_saisie.split()
		for x in texte_saisie:
			if (x.islower()):
				texte_crypter += chr((ord(x)-ord('a')-decalage)%26+ord('a'))
			elif (x.isupper()):
				texte_crypter += chr((ord(x)-ord('A')-decalage)%26+ord('A'))
			else:
				texte_crypter += x
		print(texte_crypter)

texte_saisie = raw_input("Entre ton texte à crypter: ")

print (texte_saisie.Cesar)
