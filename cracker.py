#!/usr/bin/python
#-*-coding:utf-8-*-
import itertools
p=raw_input("Entre ton prénom: ")
print("\nVous auriez pu vous appeler: ")
for x in itertools.permutations(p):
	print''.join(x)
