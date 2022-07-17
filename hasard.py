#!usr/bin/python
#-*-coding:utf-8-*-
from random import choice
from string import maketrans
from math import *
a = "éèçêâôùû"
b = "eeeecceeaaoouuuu"
conversion = maketrans(a,b)
lne = "Combien font lne²"
Racine_caree = "Combien font racine caree de 25?"
Etoile = "Combien y'a t'il d'étoile dans l'univers"
questions = ["lne²:2","racine caree de 25:5","Etoile:infini"]
sortie = ["fin","stop","bye","au revoie"]
reponse = "a"
print ("Répondre 'fin','stop','bye','au revoie'")
while reponse not in sortie:
        question = choice(questions)
        reponse = input(question.split(':')).capitalize()
        if reponse not in sortie:
            if reponse.translate(conversion) == question.split(':').capitalize():
                print ("zoo")
            else:
                print ("Tu ment, reprend",question.split(':'))
print ("Bye")
