#!/usr/bin/python
#-*-coding:utf-8-*-

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_3 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
validation = 0
a=0
message_liste = []

message = raw_input ("Ecrire le message à crypter: ")
message = message.lower()

for r in message:
	message_liste.append(r)

while validation == 0:
	decalage = input("Choisir le décalage souhaité: ")
	if 0 <= decalage <= 25:
		validation = 1

for k in range(0,26):
	alphabet_2[k] = alphabet_3[decalage+k]

for i in message:
	for j in range(0,26):
		if i == alphabet[j]:
			message_liste[a] = alphabet_2[j]
	a += 1

print ''.join(str(x) for x in message_liste)
