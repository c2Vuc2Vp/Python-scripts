#!/usr/bin/python
#-*-coding:utf-8-*-

#les instructions pour le developpement du programme debuterons par un '#' et les triples quotes seront des infos pour les utilisateurs 

import smtplib
import getpass
import sys
import os

input = raw_input

#ceci sera nos fonctions de cryptage si tu veux bien
#si tu me le permet, je pense que nos differentes fonctions doivent être definit comme suite
#c'est-à-dire que le nom de la fonction de chiffrement debute par un C
#et que le nom de la fonction de dechiffrement debute par D pour que se soi plus simple

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

#juste un script pour que tu teste le cryptage Cesar

saisie = str(raw_input("saisi ton msg a crypter la: "))
print (CCesar(saisie))
saisi = str(raw_input("saisi ton msg a decrypter la: "))
print (DCesar(saisi))

#Je galère un peu sur le DCesar. les charactères [\^_`] ne se decryptent pas.

"""cryptage Morse"""
def CMorse(self):

#en attente

	print ("en attente")

def DMorse(self):

#en attente

	print ("en attente")

"""cryptage Affine"""
def CAffine(self):

#en attente

	print ("en attente")

def DAffine(self):

#en attente

	print ("en attente")

"""cryptage RSA"""
def CRSA(self):

#en attente

	print ("en attente")

def DRSA(self):

#en attente

	print("en attente")

#Fin des fonctions de cryptage

class color :

	tcolor = '\33[0m'
	red = '\033[91m'
	white = '\033[97m' 
	blue = '\033[94m'
	green = '\033[92m'
	magenta = '\033[1;35m'
	yellow = '\33[93m'

	def disable(self):

		self.tcolor = ''
		self.red = ''
		self.white = ''
		self.blue = ''
		self.green = ''
		self.magenta = ''
		self.yellow = ''
# Menu

def __main__():

	print (color.red + """
		            ##########   """+color.blue+"""             #   #"""+color.red+"""
		        #################"""+color.blue+"""            #   #"""+color.red+"""
		     ######################"""+color.blue+"""         #   #"""+color.red+"""          
		    #########################"""+color.blue+"""      #   #"""+color.red+"""
		  ############################"""+color.blue+"""    #   #"""+color.red+"""
		 ##############################"""+color.blue+"""  #   #"""+color.red+"""
		 ###############################"""+color.blue+"""#   #"""+color.red+"""                
		###############################"""+color.blue+"""    #"""+color.red+"""                       
		##############################   #"""+color.blue+"""#"""+color.red+"""                    
		                     ########   ##                     
	       """ + color.white + """  Sensei""" + color.red + """                #####   ###
	       """ + color.white + """  D3F4lT""" + color.red + """                 ###   ###
		                      ####   ###
		 ####          ##########   ####
		 #######################   ####
		   ####################   ####
		    ##################  ####
		      ############      ##
	 """+ color.white +"""                ########        ###
		        #########        #####
		      ############      ######
		     ########      #########
		       #####       ########
		         ###       #########
	     ___        ######    ############
	       .'      #######################
		:      #   #   ###  #   #   ##
		'      ########################
		        ##     ##   ##     ##
	""")
__main__()

try:
	status = True
	while status == True :

		print (color.tcolor + "Pour le manuel d'ulisation, tape "+ color.green +"h / help / aide")
		print (color.tcolor + "Pour quitter le programme, tape "+ color.red +"quit / exit / bye")
		menu = input(color.green + "\nChiffreur 1.0 [ beta ] : ")

		if menu == "h" or menu == "aide" or menu == "help" :

#Tu peux ameliorer ou ajouter des options si tu le desir
			print(color.tcolor + "\n[1] Pour envoyer un message par opérateur mobile\n[2] pour envoyer un message via mail(Gmail ou live)\n")
		if menu == "quit" or menu == "exit" or menu == "bye":

			print ("\n\n[-] QUITTING ...")
			sys.exit(0)

		if menu == "1":

			print (color.red + "[1] Envoyer un message crypté \n[2] Décrypter un message reçu\n")
			GSM = str(input(color.red + "> "))

			if GSM == "1":

				client = TwilioRestClient()
				client.messages.create(from_= input("Entre ton numéro: "),
							to = input("Entre son numéro: "),
							body = input("Entre ton message: ")) 
			if GSM == "2":
#En attente de code qui permet de recevoir les sms
				print("En attente du code qui permet de recevoir les sms")
		if menu == "2":

			print (color.magenta + "[1] Envoyer un mail crypté\n[2] Decrypter un mail reçu")
			mail = str(input(color.magenta + "> "))

			if mail == "1":

				boucle = True
				while boucle == True:

				    try:     
				 		server_disponible = ["Gmail","Live"]
				 		compteur = 1

						for server in server_disponible:

							print "["+str(compteur)+"]"+server
							compteur += 1

						server = str(input("Selectionner votre serveur: "))

						if server == "1":

							server = "smtp.gmail.com"
							port = 587

						elif server == "2":

						server = "smtp.live.com"
						port = 465
					compte_email = input("Entrez votre addresse gmail: ")
				 	password = getpass.getpass("Entrez votre mot de passe: ")
					email = input("L'addresse de la victime: ")
					message = input("Votre message:"+color.blue+"\n\t") #Il fait egalement l'option spam
					print (color.magenta+"Message crypté a envoyer>"+color.green+CCesar(message))
					NM = input(color.magenta+"Entrez le nombre de fois que message dois être envoyé: "+color.red)  
					envoyer = 0

					try:

					    server = smtplib.SMTP(server, port)
					    server.ehlo()
					    server.starttls()
					    server.login(compte_email,password)

					    while (NM > envoyer):

						msg = "Vous avez envoyer dépuis cette addresse: "+compte_email+"\n Ce message: "+message+"\n"+str(envoyer)+"fois"

						server.sendmail(compte_email,email,message)
						envoyer += 1 

					    	print envoyer

						server.quit()

						print msg

					except KeyboardInterrupt:

					    print "Stop\n"+msg

					else:

					    print (color.red+"Aucun serveur ne correspond à votre demande!")
					    continue

				    except NameError:

					print (color.red+"Erreur. \nVeillez saisir correctement votre identifiant"+color.magenta)
					boucle = True

				    except KeyboardInterrupt:

					print ("\nFin du programme")
					exit()

			if mail == "2":
#En attente de code qui permet de recevoir les mails
				print ("En attente du code qui permet de recevoir les mails")
except KeyboardInterrupt:

	print "\nFin du programme"
	exit()
