#!/usr/bin/python
#-*-coding:utf-8-*-
import random
import string

"""chiffrement Affine revisité"""
raw_input = input

s = input(("> ").upper())
def prepare (self):
	
	lettre = ["A","B","C","D","E","F","G","H","I" "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	nombre = ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25")
	compteur = 0
	for mot in lettre:
		repl=nombre[compteur]
		for char in mot:
			s = s.replace(char,repl)
		compteur += 1
	for l in s:
		if l in ['"',"'",",",";",":","!","%","$","<",",","."]:
		    nb=s.find(l)
		    s=s[:nb]+s[nb+1:]          
	return s

prepare(s)

A = 5
B = 8
premier_calcule = (A * s + B)
deuxieme_calcule = ((A * s + B)%26)
print (deuxieme_calcule)
