#!/usr/bin/python2
#-*-coding:utf-8-*-

class color :
	tcolor = '\33[0m'
	red = '\033[91m'
	white = '\033[97m' 
	blue = '\033[94m'
	green = '\033[92m'
	magenta = '\033[1;35m'
	yellow = '\33[93m'

	def disable(self):
		self.tcolor = ''
		self.red = ''
		self.white = ''
		self.blue = ''
		self.green = ''
		self.magenta = ''
		self.yellow = ''

print ("""\t\t\033[1;91mSTRUCTURE DES PRIX INCOTERMS 2010\033[1;m"""+color.blue+"""
\tCoût de revient des matières premières
+Coût de production
+Coût de réseau de distribution
+Autres charges d'exploitation
+Commissions éventuelles échéant aux intermediaires"""+color.green+"""
=COUT DE REVIENT DES PRODUITS FINIS"""+color.blue+"""
+Marge de l'exploitation/marge commerciale du fournisseur (taux de marge)"""+color.green+"""
=PRIX EXW ... OU PRIX BORD CHAMPS USINE (PRIX EX-WORK)"""+color.blue+"""
+Expédition en conteneur ou en vrac
+Chargement du camion ou du wagon
+Pré-acheminement
+Camionnage à quai et mise sous palan
+Prestation du transitaire export (HAD)
+Douane export/droit de sortie/droit unique de sortie (DUS)
+Entreposage exprot/magasinage export
+Droit de port à l'export/taxe portuaire
+Manutention terre"""+color.green+"""
=PRIX FAS"""+color.blue+"""
+Acconage export/embarquement/frais de mise à bord/passage portuaire"""+color.green+"""
=PRIX FOB / FCA"""+color.blue+"""
          .¨+Fret de base/coût de transôrt principal
          | +BAF (bunker ajustment factor)
+Fret net<  +CAF (currency ajustment factor)
          | +CSP (congestion surcharge portuaire)/ encombrement portuaire
          ..(-) Ristourne/remise/rabais
+Frais d'émission B/L ou LTA
+Taxe B/L (taxe connaissement)/LTA"""+color.green+"""
= PRIX CFR/CPT..."""+color.blue+"""
+Assurance maritime/prime d'assurance=taux de prime x valeur d'assurance"""+color.green+"""
=PRIX CIF/CIP"""+color.blue+"""
+Acconage import/déchargement du navire/passage portuaire à l'import"""+color.green+"""
=PRIX DAT"""+color.blue+"""
+Manutention quai/magasin ou air de dédouanement, transport de la marchadise du quai
+Magasinage à destination/entreposage import
+Chargement des marchandise à quai sur moyen de transport pour post acheminement
+Post acheminement(transport de fin de parcours, camionnage à l'arrivée"""+color.green+"""
=PRIX DAP"""+color.blue+"""
+Transit import/ouverture de dossier à destination (HAD)
+Douane import (droit et taxe)
+Droit du receceur de douane/travaux supplémentaires douane (TSD)
+Redevance BIVAC SCAN:produit en conteneur(20'=66.000f et 40'=132.000f)"""+color.green+"""
=PRIX DDP"""+color.blue+"""
+Déchargement du camion/wagon chez l'importateur
+Rémunération de la société de vérification (WEBBFONTAINE)
+Frais financier"""+color.green+"""
=COÛT DE REVIENT DES MARCHANDISES IMPORTEES (considéré comme coût de revient hors taxe)"""+color.blue+"""
+Marge bébéficiaire de l'importateur(taux de marque ou taux de marge)"""+color.green+"""
=PRIX D'ACHAT DU GROSSITE (HORS TAXE)"""+color.blue+"""
+Marge bénéficiaire du grossite"""+color.green+"""
=PRIX D'ACHAT DU DÉTAILANT (HORS TAXE)"""+color.blue+"""
+Marge bénéficiaire du détaillant"""+color.green+"""
=PRIX D'ACHAT DU CONSOMMATEUR FINAL (HORS TAXE)"""+color.blue+"""
+ TVA(18%)"""+color.green+"""
=PRIX D'ACHAT DU CONSOMMATEUR FINAL (TTC)
""")
print ("\t\t\t\t\033[1;35mApplication\033[1;m")
cvt= int(input("Devise en Fcfa = "+color.white))
cvt2= int(input(""+color.tcolor+"Devise d'autre ETAT= "+color.white))
NC= int(input(""+color.tcolor+"NC > "+color.white))
NB= int(input(""+color.tcolor+"NB > "+color.white))
EXW= int(input(""+color.tcolor+"EXW > "+color.white))
EXW= float(EXW*NC)
print((""+color.green+"EXW= %d"%EXW))

Empotage_du_conteneur=int(input(""+color.tcolor+"Empotage du conteneur > "+color.white))
Pre_acheminement= int(input(""+color.tcolor+"Pré-acheminement > "+color.white))
Transit_export= int(input(""+color.tcolor+"Transit_export > "+color.white))
Douane_export= int(input(""+color.tcolor+"Douane_export > "+color.white))
Douane_export= int((Douane_export*NB)*NC)
FAS= float(EXW+Empotage_du_conteneur+Pre_acheminement+Transit_export+Douane_export)
print(""+color.green+"FAS= %d"%FAS)

Acconage_export= int(input(""+color.tcolor+"Acconage export > "+color.white))
FOB= float(FAS+Acconage_export)
print(""+color.green+"FOB= %d"%FOB)

Fret_de_base= int(input(""+color.tcolor+"Fret de base > "+color.white))
Fret_de_base= float(Fret_de_base*cvt)
BAF= int(input(""+color.tcolor+"BAF > "+color.white))
BAF= int(BAF/100)
BAF= int(BAF*Fret_de_base)
CAF= int(input(""+color.tcolor+"CAF > "+color.white))
CAF= int(CAF/100)
CAF= int(CAF*(CAF+Fret_de_base))
Fret_net= int(Fret_de_base+BAF+CAF)
CFR= float(FOB+Fret_net)
print(""+color.green+"CFR= %d"%CFR)

PA= float(input(""+color.tcolor+"PA > "+color.white))
PA= float((PA/100)*1.1)
CIF= float(1-PA)
CIF= float(CFR/CIF)
CIF= str(CIF)
print (""+color.green+"CIF= %d"%(CIF))

Acconage_import= int(input(""+color.tcolor+"Acconage import > "+color.white))
DAT= float(CIF+Acconage_import)
DAT= str(DAT)
print(""+color.green+"DAT= %d"%DAT)

Post_acheminement= int(input(""+color.tcolor+"Post acheminement > "+color.white))
DAP= float(DAT+Post_acheminement)
DAP= str(DAP)
print(""+color.green+"DAP= %d"%DAP)

DD= int(input(""+color.tcolor+"DD > "+color.white))
DD= (DD/100)
RSTA= int(input(""+color.tcolor+"RSTA > "+color.white))
RSTA= (RSTA/100)
PCS= int(input(""+color.tcolor+"PCS > "+color.white))
PCS= (PCS/100)
PCC= float(input(""+color.tcolor+"PCC > "+color.white))
PCC= (PCC/100)
TVA= int(input(""+color.tcolor+"TVA > "+color.white))
TVA= (TVA/100)
TSD= int(input(""+color.tcolor+"TSD > "+color.white))
TC= float(DD+RSTA+PCS+PCC+TVA(100+DD+RSTA))
Droit_et_Taxe= (TC*TSD)
print (Droit_et_Taxe)
