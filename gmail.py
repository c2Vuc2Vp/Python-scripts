#!/usr/bin/python
#-*-coding:utf-8-*-

import email
import imaplib
import ctypes
import getpass

mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
nu = raw_input("Entrez votre addresse mail: ")
mp = getpass.getpass("Entrez votre mot de passe")
mail.login(nu,mp)
mail.select("INBOX")
def loop():
    mail.select("INBOX")
    c = 0
    (retcode, messages) = mail.search(None,'(UNSEEN)')
    if retcode == 'OK':
        for num in messages[0].split():
            c += 1
            print c
            typ, sauvegarde = mail.fetch(num,'(RFC822)')
            for reponse in sauvegarde:
                if isinstance (reponse,tuple):
                    original = email.message_from_string(reponse[1])
                    print original['From']
                    sauvegarde = original['Sudject']
                    print sauvegarde
                    typ, data = mail.store(num,'+FLAGS','\\Seen')
if __name__ == '__name__':
    try:
        while True:
            loop()
    finally:
        print "Merci"
