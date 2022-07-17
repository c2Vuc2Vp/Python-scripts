#!/usr/bin/python
#-*-coding:utf-8-*-
import random
import string
import time
import sys, os

class ACIchiffrement :
	def __init__(self):
		self.liste = string.ascii_letters + string.digits + string.punctuation + " "

	def encrypt(self, text, password):
		msg = password + text
		print ("chiffrement de : " + msg)
		with open(".signature", "r") as file :
			content = file.read()
		content = content.split("\n")
		signa = random.choice(content)

		signa = signa.split(" ")
		signature = []
		for number in signa :
			signature.append(int(number))

		lenMsg = len(msg)
		x = 0
		y = 0
		i = 0
		MsgEncrypt = []

		while lenMsg > x :
			letter = msg[x]
			if y < 4 :
				NombreDeCaractere = signature[y]
			if y == 4 :
				y = 0
				NombreDeCaractere = signature[y]
			i = 0
			while NombreDeCaractere > i :
				NewLetter = random.choice(self.liste)
				MsgEncrypt.append(NewLetter)
				i += 1
			MsgEncrypt.append(letter)
			if y == 4 :
				y = 0
			else :
				y += 1
			x += 1

		result = "".join(MsgEncrypt)
		print ("\n" + result)
		return result, signature


	def decrypt(self, text, password, signature):
		print ("[  *  ] dechiffrement avec la signature : ", signature)
		lenText = len(text)
		Msg = []

		y = 0
		i = 0
		mod = 0

		status = True

		while i < lenText and status == True :
			try :
				while y < 4 :
					mod += signature[y]
					letterToAdd = text[mod]

					Msg.append(letterToAdd)
					mod += 1
					i += signature[y]
					y += 1
				y = 0
			except IndexError:
				return "".join(Msg)
				status = False
			except KeyboardInterrupt :
				print "[ + ] resultat avant interruption : " + "".join(Msg)
saisir = encrypt(saisir,raw_input("text> "),raw_input("pass> "))
