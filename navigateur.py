#!usr/bin/python
#-*-coding:utf-8-*-

try:
	import gtk
	import gobject
	import webkit
except ImportError:
	print ("[!] Veillez installer ces (gtk,gobject,webkit) modules avant de continuer." )

def navigateur(widget):
	browser.open("http://"+widget.get_text()) #Rajout de http:// pour  éviter de taper à chaque fois dans la ligne de saisie.

gobject.threads_init()

#Création de la fenêtre de notre naviguateur qu'on appelle fn
fn = gtk.Window()
fn.set_title("Surffer") #Nom du navigateur
fn.set_default_size(600,300) #Taille de la fenêtre du navigateur à l'ouverture
fn.set_position(gtk.WIN_POS_CENTER) #On centre la fenêtre du naviguateur à l'ouverture
fn.connect("destroy",gtk.main_quit) #Pour pouvoir fermer la fenêtre

#Création d'une Vbox, que l'on nommera v
v = gtk.VBox(10,10)
fn.add(v)

#Création d'une zone de texte qu'on nomera z
z = gtk.Entry()
gtk.Entry().set_alignment(0,5) #Pour centrer l'addresse saisie, c'est plus esthétique
z.connect("activate",navigateur) #Appel de navigateur lorsqu'on tape sur la touche entrée du clavier
v.pack_start(z,False,False,0)

browser=webkit.WebView()
v.pack_start(browser)

f.show_all()
gtk.main()
