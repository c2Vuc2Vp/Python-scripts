#!/usr/bin/python
#-*-coding:utf-8-*-

import random
import sys, os

tab = []

maxLenght = int(raw_input("max d'ecartement : "))

for i in range(4, maxLenght) :
	tab.append(str(i))

listeToGenerate = []
filename = ".signature"

i = int(raw_input("nombre de cle a generer : "))
x = 0

while x < i :
	signa = random.choice(tab) + " " + random.choice(tab) + " " + random.choice(tab) + " " + random.choice(tab) + "\n"
	print signa.replace("\n", "")

	status = True
	for blacklist in listeToGenerate :
		if signa == blacklist :
			status = False

	with open(filename, "a") as file :
		if status == True :
			file.write(signa)
			listeToGenerate.append(signa)
			x += 1
		if status == False :
			pass
