# -*- coding: Latin-1 -*-
#!/usr/bin/env python

import random

def titre(P):
    print "        ####################################"
    print "        #  Chiffrement par fonction affine #"
    print "        ####################################"
    print
    print
    print
    print
   
def prepare(PhraseEnClair):
    li1=["âà","éèêë","îï","ô","ûü","ç"]
    li2=["A","E","I","O","U","C"]
    i=0
    # Remplacement des caractères accentués éventuels  et ponctuation
    for mot in li1:
       repl=li2[i]
       for lettre in mot:
           PhraseEnClair=PhraseEnClair.replace(lettre,repl)
       i+=1
    for l in PhraseEnClair:
        if l in ['"',"'",",",";",":","!","%","$","<",",","."]:
            nb=PhraseEnClair.find(l)
            PhraseEnClair=PhraseEnClair[:nb]+PhraseEnClair[nb+1:]          
    return PhraseEnClair

def alea(P):
    aa=random.randint(0,10)
    a=P[aa]
    b=random.randint(1,25)
    codage(a,b)
    return

def perso(P):
    ok=0
    print "    --- Attention, voici la liste des nombres premiers avec 26 ---"
    print "         ",
    for n in P:
        print n,
    print
    while not ok:
        print
        aa=raw_input("Choix du coefficient a (à prendre dans la liste ci-dessus): ")
        try :
            a=int(aa)
            if a  not in P:
                print "Entrée incorrecte. Veuillez recommencer s'il vous plaît !"
            else:
                ok=1
        except ValueError:
            print "Entrée incorrecte. Veuillez recommencer s'il vous plaît !"
    ok=0    
    while not ok:
        aa=raw_input("Entrer le npmbre b (doit être compris entre 0 et 25) : ")
        try :
            b=int(aa)
            if b<0 or b>25:
                print "Entrée incorrecte. Veuillez recommencer s'il vous plaît !"
            else:
                ok=1
        except ValueError:
            print "Entrée incorrecte. Veuillez recommencer s'il vous plaît !"
    print
    return a,b

def codage(a,b):
    ######## Ecrire, ci-dessous, entre les guillemets, votre phrase ########
       
    Acrypter = "Euler, le grand mathématicien, a donné une règle permettant \
de résoudre tous les problèmes de labyrinthes et qui consiste \
essentiellement à chercher un chemin depuis la sortie."

    ########################################################################
    Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    PhraseEnClair=Acrypter
    PhraseEnClair=prepare(PhraseEnClair).replace(" ","").upper()
    lg=len(PhraseEnClair)
    PhraseCodee=""
    for i,lt in enumerate(PhraseEnClair):
        pos = Alpha.find(lt)
        PhraseCodee+=Alpha[(a*pos+b)%26]  
    affichage(Acrypter,PhraseCodee,lg,a,b)
    return  

def affichage(Acrypter,PhrC,lg,a,b):
    # Préparation du message de sortie en groupes de 5 lettres séparés
    # par une espace    
    coupes=lg/5-(lg%5==0)
    for i in xrange(coupes):
        # Insertion d'un espace tous les 5 caractères dans PhraseCodee
        PhrC=PhrC[0:5+6*i]+" "+PhrC[5+6*i:lg]
        lg+=1
    # Affichage du résultat
    print
    print
    print 'Clé : ('+ str(a) + ' ; '+ str(b)+')'
    print
    print "                 Message d'origine :"
    print Acrypter
    print
    print "                 Message codé :"
    print PhrC
    print
    print
    print
    return

   
P= [3,5,7,9,11,15,17,19,21,23,25]
titre(P)
while 1:
    print "A- Choix aléatoire du code"
    print "B- Vous choisissez vous-même votre code"
    print "      Q- Quitter le programme ?"
    print
    print "           *** Votre Choix *** "
    rep=raw_input("                     ")
    rep=rep.upper()
    if rep not in "ABQ":
        print
        print "Erreur - Recommencez s'il vous plaît !"
        print
    elif rep=="A":
        alea(P)
    elif rep=="B":
        a,b=perso(P)
        codage(a,b)
    else:
        break
print
print"          Au revoir !"
