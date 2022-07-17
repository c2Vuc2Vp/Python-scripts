#!/usr/bin/python
#-*-coding:utf-8-*-

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_3 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
validation = 0
a,b,c = 0,0,0
z = 0
encodecode = ["Encode","Decode"]
compteur = 1

boucle = True
print("	                      ########                  #")
print("                #################            #")
print("             ######################         #")
print("            #########################      #")
print("          ############################")
print("         ##############################")
print("         ###############################")
print("        ###############################")
print("        ##############################")
print("                        #    ########   #")
print("           Sensei              #####            ####   ##")
print("                                ###   ###")
print("                              ####   ###")
print("         ####          ##########   ####")
print("         #######################   ####")
print("           ####################   ####")
print("            ##################  ####")
print("              ############      ##")
print("                 ########        ###")
print("                #########        #####")
print("              ############      ######")
print("             ########      #########")
print("               #####       ########")
print("                 ###       #########")
print("     ___        ######    ############")
print("       .'      #######################")
print("        :      #   #   ###  #   #   ##")
print("        '      ########################")
print("                ##     ##   ##     ##")
while boucle:
	try:
		for w in encodecode:

			print ("["+(str(compteur))+"]"+w)

			compteur += 1

		w = input("Faites votre choix: ")
		if (z < w < compteur):
			if (encodecode[w-1] == "Encode"):
				message_liste = []
				message = raw_input ("Ecrire le message à crypter: ")
				message = message.lower()

				for r in message:
					message_liste.append(r)

				while validation == 0:
					decalage = input("Choisir le décalage souhaité (0...25): ")
					if 0 <= decalage <= 25:
						validation = 1

				for k in range(0,26):
					alphabet_2[k] = alphabet_3[decalage+k]

				for i in message:
					for j in range(0,26):
						if i == alphabet[j]:
							message_liste[a] = alphabet_2[j]
					a += 1

				print (''.join(str(x) for x in message_liste)+"\n")
				continue
			elif (encodecode[w-1] == "Decode"):
				message_liste = []
				message = raw_input("Ecrire le message à decrypter: ")

				for r in message:
					message_liste.append(r)

				for d in range(0,26):
					for e in message:
						for g in range(0,26):
							if e == alphabet[g]:
								message_liste[c] = alphabet_3[g+b]
						c += 1
					c = 0
					b +=1
					print (''.join(str(x) for x in message_liste))
					print ('')

	except KeyboardInterrupt:
		print ("\nfin")
		exit()
	except NameError:
		print ("[!] Veillez taper un chiffre entre 1 et 2\n")
		continue