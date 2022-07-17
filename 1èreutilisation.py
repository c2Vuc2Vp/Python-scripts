#!/usr/bin/python
#-*-coding:utf-8-*-
import os
import sys, traceback

notRoot = False
try:
    # verifier si l'utilisateur est root
    if os.geteuid() != 0:
        print("\n\033[1;91mERROR: Ce script doit être lancé avec le privilège root. Essayer avec sudo:\n\tsudo python 1èreutilisation.py\033[1;m\n")
        notRoot = True
except:
    pass
if notRoot:
    raise SystemExit

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

def main():
	try:
		print (color.red + """
		            ##########   """+color.blue+"""             #   #"""+color.red+"""
		        #################"""+color.blue+"""            #   #"""+color.red+"""
		     ######################"""+color.blue+"""         #   #"""+color.red+"""          
		    #########################"""+color.blue+"""      #   #"""+color.red+"""
		  ############################"""+color.blue+"""    #   #"""+color.red+"""
		 ##############################"""+color.blue+"""  #   #"""+color.red+"""
		 ###############################"""+color.blue+"""#   #"""+color.red+"""                
		###############################"""+color.blue+"""    #"""+color.red+"""                       
		##############################   #"""+color.blue+"""#"""+color.red+"""                    
		                     ########   ##                     
	       """ + color.white + """  Sensei""" + color.red + """                #####   ###
		                       ####   ###
		 ####          ##########   ####
		 #######################   ####
		   ####################   ####
		    ##################  ####
		      ############      ##
	 """+ color.white +"""                ########        ###
		        #########        #####
		      ############      ######
		     ########      #########
		       #####       ########
		         ###       #########
	     ___        ######    ############
	       .'      #######################
		:      #   #   ###  #   #   ##
		'      ########################
		        ##     ##   ##     ##
	""")
		def aide():
			print ("\n\033[1;32m-Taper retour pour revenir au menu des installations\n-Taper menu pour revenir à la page d'acceuille\n-Taper le/un des numéros de la liste affichée\n-Taper aide pour avoir l'aide\n\033[1;m")
		try:
			def menu():
				print ("\033[1;32mTaper aide/h pour avoir l'aide\n\033[1;m")
				print("\033[0m[1]Installation des paquets\n\033[1;36m[2]Installation des outils github\n\033[1;m")
				option0 = (raw_input("\033[1;36m> \033[1;m"))
				try:
					def menu1():
						while option0 == "1":
							print ("[1]Installer les paquets")
							installation = (raw_input("\033[1;36m> \033[1;m"))
							if installation == "1":
								pakets = os.system("apt-get -f install qbittorrent net-tools irssi vlc vim youtube-dl python-pip python3-pip gscan2pdf git kdeconnect zenmap wireshark gparted ettercap-graphical wget ettercap-pkexec acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood manpage-fr pdfcrack netcat ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree macchanger metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif installation == "retour":
								menu()
							elif installation == "menu":
								main()
							elif installation == "h":
								aide()
							elif installation == "aide":
								aide()
							else:
								print("\n\033[1;91mVotre commande est introuvable\033[1;m")
								aide()

						while option0 == "2":
							print ("\n[1]Installation de Setoolkit\n\033[1;36m[2]Installation de Metasploit\033[1;m\n[3]Installation de Kickthemout\n\033[1;36m[4]Installation de Katoolin\n\033[1;m[5]Installation de TheFatRat\n\033[1;36m")
							github = raw_input("\033[1;36m> \033[1;m")

							while github == "1":
								print ("[1]Installation des dependances de Setoolkit\n\033[1;36m[2]Installation à proprement dit\n\033[1;m")
								installation = (raw_input("\033[1;36m> \033[1;m"))
								if installation == "1":
									setoolkit = os.system("apt-get --force-yes -y install git apache2 python-requests libapache2-mod-php \  python-pymssql build-essential python-pexpect python-pefile python-crypto python-openssl")
								elif installation == "2":
									endroit = os.system("cd /opt/")
									gitclone = os.system("git clone https://github.com/trustedsec/social-engineer-toolkit.git")
									endroit1 = os.system("cd social-engineer-toolkit/")
			 						installation2 = os.system("python setup.py install")
									print ("\nFin de l'installation de Setoolkit\n")
								elif installation == "retour":
									menu1()
								elif installation == "menu":
									main()
								elif installation == "h":
									aide()
								elif installation == "aide":
									aide()
								else:
									print("\n\033[1;91mVotre commande est introuvable\033[1;m")
									aide()

							while github == "2":
								print("En attente")

							while github == "3":
								print ("[1]Installation à proprement dit\n")
								installation = (raw_input("\033[1;36m> \033[1;m"))
								if installation == "1":
									endroit = os.system("cd /opt/")
									gitclone = os.system("git clone git clone https://github.com/k4m4/kickthemout.git")
									endroit1 = os.system("cd kickthemout/")
									dependance1 = os.system("sudo -H pip install --upgrade pip")
									dependance2 = os.system("sudo -H python -m pip install -r requirements.txt")
									installation2 = os.system("cp kickthemout/kickthemout.py /usr/bin/kickthemout && chmod +x /usr/bin/kickthemout")
									print ("\nFin de l'installation de Kickthemout\n")
								elif installation == "retour":
									menu1()
								elif installation == "menu":
									main()
								elif installation == "h":
									aide()
								elif installation == "aide":
									aide()
								else:
									print("\n\033[1;91mVotre commande est introuvable\033[1;m")
									aide()

							while github == "4":
								print ("[1]Installation à proprement dit\n")
								installation = (raw_input("\033[1;36m> \033[1;m"))
								if installation == "1":
									endroit = os.system("cd /opt/")
									gitclone = os.system("git clone https://github.com/LionSec/katoolin.git")
									endroit1 = os.system("cp katoolin/katoolin.py /usr/bin/katoolin")
									installation2 = os.system("chmod +x /usr/bin/katoolin")
									print ("\nFin de l'installation de Katoolin\n")
								elif installation == "retour":
									menu1()
								elif installation == "menu":
									main()
								elif installation == "h":
									aide()
								elif installation == "aide":
									aide()
								else:
									print("\n\033[1;91mVotre commande est introuvable\033[1;m")
									aide()
							while github == "5":
								print ("[1]Installation à proprement dit\n")
								installation = (raw_input("\033[1;36m> \033[1;m"))
								if installation == "1":
									endroit = os.system("cd /opt/")
									gitclone = os.system("git clone https://github.com/Screetsec/TheFatRat.git")
									endroit1 = os.system("cd TheFatRat/")
									installation2 = os.system("chmod +x setup.sh && ./setup.sh")
									print ("\nFin de l'installation de Kickthemout\n")
								elif installation == "retour":
									menu1()
								elif installation == "menu":
									main()
								elif installation == "h":
									aide()
								elif installation == "aide":
									aide()
								else:
									print("\n\033[1;91mVotre commande est introuvable\033[1;m")
									aide()
							while github == "retour":
								menu()
								break
							while github != "1" and github != "2" and github != "3" and github != "4" and github != "5" and github != "6":
								print("\n\033[1;91mVotre commande est introuvable\033[1;m")
								aide()
								break
						while option0 == "menu":
							menu()
						while option0 == "h" or option0 == "aide":
							aide()
							menu()
						while option0 != "1" and option0 != "2":
							print("\n\033[1;91mVotre commande est introuvable\033[1;m")
							aide()
							break
						
					menu1()
				except KeyboardInterrupt:
					menu1()
			menu()
		except KeyboardInterrupt:
			menu()
	except KeyboardInterrupt:
		print ""
		print ("\n\033[1;91mFin du programme demander...Goodbye...\033[1;m\n")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)
if __name__ == "__main__":
	main()
