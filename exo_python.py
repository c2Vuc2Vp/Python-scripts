#!/usr/bin/python
#-*-coding:utf-8-*-


######################## EXO 4.2 ####################################

print ("EXO4.2\nEcrivez un programme qui affiche les 20 premiers termes de la table de\nmultiplication par 7")

print("\n")# Début de l'exercice

a = 0
m = 0

while a < 21:

	print ("7 *",a,"=",7 * m)
	m += 1
	a += 1

print("\n\n")# Fin de l'excercice

######################## EXO 4.3 ####################################

print("""EXO4.3\nEcrivez un programme qui affiche une table de conversion de sommes d'argent\nexprimee en euros, en dollars canadiens. La programmation des sommes de la table\nsera << geometrique >>, comme dans l'exemple ci-dessous :
1 euro(s) = 1.65 dollar(s)
2 euro(s) = 3.30 dollar(s)
4 euro(s) = 6.60 dollar(s)
8 euro(s) = 13.20 dollar(s)
ets. (S'arreter à 16384 euros.)""")

print("\n")# Début de l'exercice

ce,cd=1,1.65

while ce<16385:

	print (ce,'euro(s) =',cd,'dollar(s)')
	ce*=2
	cd*=2

print("\n\n")#Fin de l'excercice

######################## EXO 4.4 ####################################

print("EXO4.4\nEcrivez un programme qui affiche une suite de 12 nombres dont chaque terme soit\negal au triple du terme precedent.")

print("\n")# Début de l'exercice

a,b=1,1

while b<13:

	print (a)
	a*=3
	b+=1

print("\n\n")#Fin de l'excercice

######################## EXO 4.5 ####################################

print("EXO4.5\nEcrivez un programme qui calcule le volume d'un parallelepipede rectangle\ndont sont fournis au départ la largeur, la hauteur et la profondeur.")

print("\n")# Début de l'exercice

from math import *

l = int(input("Entre la largeur: ")) # l = largeur
h = int(input("Entre la hauteur: ")) # h = hauteur
p = int(input("Entre la profondeur: ")) # p = profondeur
v= h * p * l # v = volume

print ("Volume :",v)

print("\n\n")#Fin de l'excercice

######################## EXO 4.6 ####################################

print("EXO4.6\nEcrivez in programme qui convertit un nombre entier de seconde fourni au départ\nen un nombre d'annees, de mois, de semaines, de jours, d'heures, de\nminutes et secondes (utilisez l'operateur modulo: %)")

print("\n")# Début de l'exercice

compteur = 1
sec = 1
mn = 60 * 1
h = 60 * mn
j = 24 * h
sem = 7 * j
m_f = 27.5 * sem # Le mois de Février
m = 30 * sem # Les mois de 30 jours
m_l = 31 * sem # Les mois de 31 jours
a = 12 * ((m * 7) + ( m_l * 4) + m_f)

sa= int(input("Notez le nombre de seconde que vous voulez convertir: "))
print("les secondes entrées sont égales à: ", a, "an/" , m_l, "secondes en mois de 31 jours\nou", m, "secondes en mois de 30 jours ou", m_f, "secondes en fevrier", sem, "secondes en semaines\n", j, "secondes en jours", h, "secondes en heures", mn, "secondes en minutes")

######################## EXO 4.7 ####################################

print("EXO4.7\nEcrivez un programme qui affiche les 20 premiers termes de la table de multiplication\npar 7, en signalant au passage (à l’aide d’une astérisque)\nceux qui sont des multiples de 3. Exemple :   7   14   21 * 28   35   42 * 49 ...")

print("\n")# Début de l'exercice

a = 0
m = 0

while a < 21:

	if (m%3==0 and m>0):
		print (7 * m,'*')
	else:
		print (7 * m)
	m += 1
	a += 1

print("\n\n")# Fin de l'excercice

######################## EXO 4.8 ####################################

print("EXO4.8\nÉcrivez un programme qui calcule les 50 premiers termes de la table de multiplication\npar 13, mais n’affiche que ceux qui sont des multiples de 7.")

print("\n")# Début de l'exercice

a = 0
m = 0

while a < 51:

	if (m%7==0 and m>0):
		print (13 * m)

	m += 1
	a += 1

print("\n\n")# Fin de l'excercice

######################## EXO 4.9  ####################################

print("EXO4.9\n Écrivez un programme qui affiche la suite de symboles suivante : \n*\n**\n***\n****\n*****\n******\n******* ")

print("\n")# Début de l'exercice

c = 0
s = ("*")

while c <= 7:
	print(s*c)
	c += 1
	

print("\n\n")# Fin de l'excercice

######################## EXO  ####################################

print("EXO\n")

print("\n")# Début de l'exercice



print("\n\n")# Fin de l'excercice

######################## EXO  ####################################

print("EXO\n")

print("\n")# Début de l'exercice



print("\n\n")# Fin de l'excercice

######################## EXO  ####################################

print("EXO\n")

print("\n")# Début de l'exercice



print("\n\n")# Fin de l'excercice

######################## EXO  ####################################

print("EXO\n")

print("\n")# Début de l'exercice



print("\n\n")# Fin de l'excercice

######################## EXO  ####################################

print("EXO\n")

print("\n")# Début de l'exercice



print("\n\n")# Fin de l'excercice

######################## EXO  ####################################

print("EXO\n")

print("\n")# Début de l'exercice



print("\n\n")# Fin de l'excercice

######################## EXO  ####################################

print("EXO\n")

print("\n")# Début de l'exercice



print("\n\n")# Fin de l'excercice
