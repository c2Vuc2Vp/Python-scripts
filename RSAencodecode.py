#!/usr/bin/python
#-*-coding:utf-8-*-

import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplication_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

'''
Teste pour vérifier que le nombre est premier.
'''
def est_premier(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generer_paire_de_cle(p, q):
    if not (est_premier(p) and est_premier(q)):
        raise ValueError('[!] Les nombres doivent être premier.')
    elif p == q:
        raise ValueError('p et q ne peuvent pas être egaux')
    #n = pq
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplication_inverse(e, phi)
    
    #Retourner la paire de clée pubique et privée
    #Clée publique est (e, n) et clée privée est (d, n)
    return ((e, n), (d, n))

def CRSA(pk, texte_saisie):
    cle, n = pk
    #Convertir chaque lettre de texte_saisie en nombre basé sur le caractère utilisant a^b mod m
    chiffreur = [(ord(char) ** cle) % n for char in texte_saisie]
    return chiffreur

def DRSA(pk, texte_crypter):
    cle, n = pk
    #Générer le text_saisie à partir du texte_crypter et une clé utilisant a^b mod m
    plan = [chr((char ** cle) % n) for char in texte_crypter]
    return ''.join(plan)
    

if __name__ == '__main__':
    '''
    Detecte si le script est directement lancé par l'utilisateur
    '''
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
    print "RSA crypteur/ Decrypteur"
    print ("Exemple de nombre premier")
    print (FirstNumbers[:400])
    p = int(raw_input("Entre ton nombre premier: "))
    q = int(raw_input("Entre un autre nombre premier (Pas celui qui vous avez deja entré): "))
    print "Génération de vos paires de clés publique et privée . . ."
    publique, privee = generer_paire_de_cle(p, q)
    print ("Votre clé publique est ", publique ," et votre clé privée est ", privee)
    message = raw_input("Entrer votre message à crypter avec votre clé privée: ")
    msg_crypte = CRSA(privee, message)
    print ("Votre message crypter est: ")
    print ''.join(map(lambda x: str(x), msg_crypte))
    print "Décryptage du message avec votre clé publique ", publique ," . . ."
    print "Votre message est:"
print DRSA(publique, msg_crypte)
