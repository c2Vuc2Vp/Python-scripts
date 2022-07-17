import random
import string
import hashlib
import sys
import os

input = raw_input
# Mes fonctions de matheu x)

def PGCD(a, b):
	while b != 0 :
		a, b = b, a % b
	return a

def Nombre_Premier(x):
	if x == 2 :
		return True
	if x < 2 or x % 2 == 0 :
		return False
	for n in xrange(3, int(x ** 0.5) + 2, 2):
		if x % n == 0 :
			return False
	return True

def multiplication_inverser(e, PhiDeN):
	d = 0
	x1 = 0
	x2 = 1
	y1 = 1
	temporaire_phi = PhiDeN

	while e > 0 :
		tempo1 = temporaire_phi / e
		tempo2 = temporaire_phi - tempo1 * e
		temporaire_phi = e
		e = tempo2
		x = x2 - tempo1 * x1
		d = tempo1 * y1
		y = d
		x2 = x1
		x1 = x
		d = y1
		y1 = y

	if temporaire_phi == 1 :
		return d + PhiDeN

# un peu de couleur sur le terminal x)

class color :
	TColor = '\33[0m'
	red = '\033[91m'
	white = '\033[97m' #tous les terminaux non pas '\33[0m' comme couleur blanche par defaut
	blue = '\033[94m'
	green = '\033[92m'
	magenta = '\033[1;35m'
	yellow = '\33[93m'

	def disable(self):
		self.TColor = ''
		self.red = ''
		self.white = ''
		self.blue = ''
		self.green = ''
		self.magenta = ''
		self.yellow = ''


# Ma classe contenant ma methode de chiffrement ( algo RSA, hash etc ... )

class Message_Secure :
	def __init__(self, p, q):
		self.ninja = color.green + """
                    ##########                #
                #################            #
             ######################         #
            #########################      #
          ############################    #
         ##############################  #
         ###############################
        ###############################
        ##############################   #
                             ########   ##
       """ + color.red + """    Sensei""" + color.green + """              #####   ###
       """ + color.blue + """      D3F4lT""" + color.green + """             ###   ###
                              ####   ###
         ####          ##########   ####
        #######################   ####
           ####################   ####
            ##################  ####
              ############      ##
                 ########        ###
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

	"""
		self.MD5 = hashlib.md5()
		self.SHA1 = hashlib.sha1()
		self.SHA224 = hashlib.sha224()
		self.SHA256 = hashlib.sha256()
		self.SHA384 = hashlib.sha384()
		self.SHA512 = hashlib.sha512()

		self.p = p
		self.q = q

	def GenerateKey(self):
		if not Nombre_Premier(self.p) and Nombre_Premier(self.q):
			return "Erreur de Valeur", "choisir des nombres premiers"
		if self.p == self.q :
			return "Erreur de valeur", "P et Q ne peuvent pas etre egal"

		n = self.p * self.q
		PhiDeN = (self.p - 1) * (self.q - 1)
		e = random.randrange(1, PhiDeN)
		g = PGCD(e, PhiDeN)
		x = e
		while g != 1 :
			while e == x :
				e = random.randrange(1, PhiDeN)
			x = e
			g = PGCD(e, PhiDeN)
		d = multiplication_inverser(e, PhiDeN)
		return ((e, n), (d, n))

	def Encrypt(self, Public_Key, message):
		key, n = Public_Key
		Message_Encrypt = [(ord(char) ** key) % n for char in message]
		return Message_Encrypt

	def Decrypt(self, Private_Key, message):
		key, n = Private_Key
		Message_Decrypt = [(chr(char) ** key) % n for char in message]
		return ''.join(Message_Decrypt)

# Et la j'appelle ma classe et je l'exploite correctement
# hesite pas si tu veux changer des trucs ou si tu veux ameliorer le code

FirstNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013,
1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069,
1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151,
1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223,
1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291,
1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373,
1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451,
1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511,
1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583,
1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657,
1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733,
1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811 ]
def __main__():
	status = True
#jai mis le ninja la car je trouve cela fait plus cool au lancement du programme
	print (color.green + """
                    ##########                #
                #################            #
             ######################         #          
            #########################      #
          ############################    #
         ##############################  #
         ###############################
        ###############################
        ##############################   #
                             ########   ##
       """ + color.red + """    Sensei""" + color.green + """              #####   ###
       """ + color.blue + """      D3F4lT""" + color.green + """             ###   ###
                              ####   ###
         ####          ##########   ####
        #######################   ####
           ####################   ####
            ##################  ####
              ############      ##
                 ########        ###
                #########        #####
              ############      ######
             ########      #########
               #####       ########
                 ###       #########
     ___        ######    ############
       .'      #######################
        :      #   #   ###  #   #   ##
        '      ########################
                ##     ##   ##     ##""")
	while status == True :
		print (color.TColor + "Pour le manuel d'ulisation, tape "+ color.green +"h / help / aide")
		print (color.TColor + "Pour quitter le programme, tape "+ color.red +"quit / exit / bye")
		menu = input(color.green + "\nChiffreur 1.0 [ beta ] : ")
		if menu == "h" or menu == "aide" or menu == "help" :
			print (color.red + "\nchoisir une fonction : " + color.white + "\n\n\t- 1 ; GeneK ; GK \t permet de creer des clees aleatoirement\n\t- 2 ; CreateK ; CK \t permet de creer ses propres clees avec les nombres que l'on choisi\n\t- 3 ; encrypt ; E \t chiffre un message ( necessite une cles publique )\n\t- 4 ; decrypt ; D \t dechiffre un message ( necessite une cles privee associer a la cles publique de chiffrement )")

		if menu == "quit" or menu == "exit" or menu == "bye":
			print ("\n\n[-] QUITTING ...")
			sys.exit(0)

		if menu == "1" or menu == "GK" or menu == "GeneK" :
			p = random.choice(FirstNumbers)
			q = random.choice(FirstNumbers)
			print (color.blue + "valeur de p : " + str(p))
			print ("valeur de q : " + str(q) + "\n")
			print (color.yellow + "Generation des cles ...\n")
			Generate = Message_Secure(p, q)
			result = Generate.GenerateKey()
			if result[0] == "Erreur de Valeur" :
				print (color.red + "\n\n[-] Erreur lors de la generation des cles : " + result[1])
			else :
				print color.red, "\nla cle publique est : ", color.blue, result[0]
				print color.red, "la cle privee est : ",color.blue, result[1], "\n"

		if menu == "2" or menu == "CK" or menu == "CreateK" :
			p = int(input(color.green + "valeur de " + color.blue + "P" + color.green + " ( cela doit etre un nombre premier ) : "))
			q = int(input("valeur de " + color.blue + "Q" + color.green + " ( cela doit etre un nombre premier ) : "))
			Create = Message_Secure(p, q)
			result = Create.GenerateKey()
			if result[0] == "Erreur de Valeur" :
				print (color.red + "\n\n[-] Erreur lors de la generation des cles : " + result[1])
			else :
				print (color.red, "\nla cle publique est : ",color.blue, result[0])
				print (color.red, "la cle privee est : ", color.blue, result[1])

		if menu == "3" or menu == "E" or menu == "encrypt" :
			message = input(color.blue + "message a chiffrer : " + color.white)
			Public_Key = input(color.green + "cle pulic : " + color.red)
			Public_Key = Public_Key.split(" ")
			if len(Public_Key) == 2 :
				a = int(Public_Key[0])
				b = int(Public_Key[1])
			if len(Public_Key) != 2 :
				print (color.green + "la cle public ne possede que deux facteurs ... exemple : 32342 29384 \nessayer de d'ecrire la cle publique en separant les facteurs par un espace\n")
				sys.exit(0)
			Public_Key = (a, b,)
			Chiffre = Message_Secure(False, False)
			result = Chiffre.Encrypt(Public_Key, message)
			print (color.white + "[" + color.green + "  result  " + color.white + "] resultat : " + str(result))

		if menu == "4" or menu == "D" or menu == "decrypt" :
			message = input(color.blue + "message a dechiffrer : " + color.white)
			Private_Key = input(color.green + "cle privee : " + color.red)
			Private_Key = Private_Key.split(" ")
			if len(Private_Key) == 2 :
				a = int(Private_Key[0])
				b = int(Private_Key[1])
			if len(Private_Key) != 2 :
				print (color.green + "la cle privee n'a que deux facteurs... exemple : 459023 30585 \nessayer d'ecrire la cle privee avec un espace entre ces deux facteurs\n")
				sys.exit(0)
			Private_Key = (a, b,)
			Dechiffre = Message_Secure(False, False)

			theMessage = []
			message = message.split(" ")
			for num in message :
				theMessage.append(int(num))

			result = Dechiffre.Decrypt(Private_Key, theMessage)
			print  (color.white + "[" + color.green + "  result  " + color.white + "] resultat : " + str(result))
__main__()
