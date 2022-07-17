# encoding: utf-8

# La fonction PGCD avec ses 2 arguments a et b
def pgcd(a,b):
    # L'algo PGCD
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a;
	
# La fonction factoriser avec en argument n
def factoriser(n):
    b=2
    while b:
        while n%b!=0 :
            b=b+1
        if n/b==1 :
            print "p = ", b,
            # On crée une variable global p pour la réutiliser hors de la fonction et p=b
            global p
            p = b
            break
        print "\nq = ", b,
        # On crée une variable global q pour la réutiliser hors de la fonction et q=b
        global q
        q=b
        n=n/b;
		
pqconnu = 0
pqconnu = input("Si vous etes en possession de p et q, entrez 1 sinon 0 : ")

if pqconnu == 0 :	
	
	# On récupère n
	n = input("Entrez le nombre n : ")

	# On appelle la fonction pour le factoriser
	factoriser(n)

	# On calcul phi(n)
	phiden = (p-1)*(q-1)

	# Variable pour notre boucle while
	compteur = 0
	PGCD1 = 0

	# Notre e qui s'incrémentera
	e = 0

	# Tant que PGCD de e et phi(n) différent de 1
	while PGCD1 != 1 :
	    # Tant que compteur=0
	    while compteur == 0 :   
	        # Si p inférieur à e et si q inférieur à e et si e inférieur à n
	        if((p < e)and(q < e)and(e < phiden)) :
	            # La boucle se coupe (on peut aussi mettre le mot-clé : break
	            compteur = 1     
	        # Tant que rien n'est trouvé, e s'incrémente
	        e = e + 1
	    # On récupère le résultat du pgcd   
	    PGCD1 = pgcd(e,phiden)

	# On calcul d
	d = 0
	compteur = 0
	
	while compteur == 0:
		# Les conditions vu ci-dessus :
		if((e * d % phiden == 1)and(p < d)and(q < d)and(d < phiden)):
		    compteur = 1
		d = d + 1
        d = d - 1

	# On affiche la clé privé
	print "\nCle privee (",d,",",n,")"
	
if pqconnu == 1 :
    p = input("Entrez le nombre p : ")
    q = input("Entrez le nombre q : ")

    # On calcul n
    n = p*q

    # On calcul phiden
    phiden = (p-1)*(q-1)

    #On demande d
    d = input("Entrez le nombre d : ")
	
# On récupère le nombre de lettre crypté (soit des bloc de un caractère)
i = input("Combien il y a de bloc :")

compteur = 0

# Tant que r inférieur au nombre de lettre
while compteur < i :
    # L'utilisateur entre le premier bloc a décrypté
    lettre_crypt = input("\nEntree le bloc a decrypte :")
    # On trouve le ASCII de chaque lettre par le calcul de décodage
    ascii = (pow(lettre_crypt,d)%n)
    # Avec la fonction chr(ASCII), on trouve le caractère correspondant
    print "lettre :",chr(ascii),
    compteur = compteur + 1	
	
# On bloque le programme avant la fermeture
raw_input('\n\nFin\n\n')
