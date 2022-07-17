#!/usr/bin/python3
#-*-coding:utf-8-*-
from random import *
import itertools
pw=[]
n=0
c=int(input("Entre la longueur de PW: "))
cc=int(input("Entre le nombre de tentative: "))
while n<cc:
	n+=1
	for x in range(c):
		pw=randrange(10)
		print((pw),end='')
	print("\r")
a=str(pw)
for x in itertools.permutations(a):
	print(x,end='')
"""
for x in range(c):
	pw=randrange(10)
	print (pw, end='')
while n<c:
    l.append(n)
    n+=1
    if (n)<=(c):
        print("\n")
        print(l, end='')
"""
	
