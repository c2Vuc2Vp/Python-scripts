#!/usr/bin/python
#-*-coding:utf-8-*-

"""
spammail Version 1.1 py par Sensei 
"""
import smtplib
import getpass

boucle = True

while boucle:

    try:

        print ("\33c")
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
 
        server_disponible = ["Gmail","Live"] 
	compteur = 1

	for server in server_disponible:

	    print "["+str(compteur)+"]"+server

	    compteur += 1

	server = input("Selectionner votre serveur: ")

	if (0 < server < compteur):

            if (server_disponible[server-1] == "Gmail"):

                server = "smtp.gmail.com"
                port = 587

            elif (server_disponible[server-1] == "Live"):

                server = "smtp.live.com"
		port = 465
	    compte_email = raw_input("Entrez votre addresse gmail: ")
 	    password = getpass.getpass("Entrez votre mot de passe: ")
	    email = raw_input("L'addresse de la victime: ")
	    message = raw_input("Votre message:\n\t")
            NM = input("Entrez le nombre de fois que message dois ??tre envoy??: ") #Nombre d'email souhait?? 
	    envoyer = 0

	try:

            server = smtplib.SMTP(server, port)
            server.ehlo()
            server.starttls()
	    server.login(compte_email,password)

	    while (NM > envoyer):

		msg = "Vous avez envoyer d??puis cette addresse: "+compte_email+"\n Ce message: "+message+"\n"+str(envoyer)+"fois"

		server.sendmail(compte_email,email,message)
		envoyer += 1 

	    	print envoyer

		server.quit()

	        print msg

	except KeyboardInterrupt:

            print "Stop\n"+msg

	else:

            print "Aucun serveur ne correspond ?? votre demande!"
	    continue

    except NameError:

        print "Erreur. \nVeillez saisir correctement votre identifiant"
	continue

    except KeyboardInterrupt:

	print "\nFin du programme"
	exit()

#J'aurais besoin de ton aide avec la version 2.

"""Dans la version 2, je voudrais qu'il y ai bien plus de serveur, que l'utilisateur ai
l'option de saisie son addresse et son password,
qu'il ai la possibilit?? d'entrer l'addresse de la victime
et ai la main libre de choisir le message et le nombre de message ?? envoyer 
sans pour autant modifier le code ?? chaque fois"""

#C'est grace ?? toi que j'en suis l?? 
#Merci pour tout ce que tu fais pour moi.
