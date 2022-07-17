#!/usr/bin/python
#-*-coding:utf-8-*-

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a = 0
b = 0
message_liste = []
message = raw_input("Ecrire le message à decrypter: ")

try:
	while True:
		for r in message:
			message_liste.append(r)

		for k in range(0,26):
			for i in message:
				for l in range(0,26):
					if i == alphabet[l]:
						message_liste[a] = alphabet_2[l+b]
				a += 1
			a = 0
			b +=1
			print ''.join(str(x) for x in message_liste)
			print ''
			continue
except KeyboardInterrupt
	print "Fermeture du programme."	
