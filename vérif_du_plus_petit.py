#!/usr/bin/python
#-*-coding:utf-8-*-

#Les 3 réels.

p = float(input("Entre le premier réel: ")) #p est le premier réel
d = float(input("Entre le deuxième réel: ")) #d est le deuxième réel
t = float(input("Entre le troisième réel: ")) #t est le troisième réel

if t < d and t < p :
	print (t,"est plus petit que", p, "et", d)
elif d < p and d < t:
	print (d, "est plus petit que", p, "et", t)
elif p < d and p < t:
	print (p, "est plus petit que", d, "et", t)
