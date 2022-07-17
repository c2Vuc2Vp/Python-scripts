#!/usr/bin/python
#-*-coding:utf-8-*-
#Sends all files per Mail
#Example usage: python sendMail.py file1.txt, file2.txt ...
import sys, smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email import Encoders

class SendMail(object):
  mailadress = 'user.name@gmail.com'
  smtpserver = 'smtp.googlemail.com'
  username = 'user.name'
  password = 'secret'

  def send(self, files):
    # Gather information, prepare mail
    to = self.mailadress
    From = self.mailadress
    #Subject contains preview of filenames
    if len(files) <= 3: subjAdd = ','.join(files)
    if len(files) > 3: subjAdd = ','.join(files[:3]) + '...'
    subject = 'Dateiupload: ' + subjAdd
    msg = self.prepareMail(From, to, subject, files)

    #Connect to server and send mail
    server = smtplib.SMTP(self.smtpserver)
    server.ehlo() #Has something to do with sending information
    server.starttls() # Use encrypted SSL mode
    server.ehlo() # To make starttls work
    server.login(self.username, self.password)
    failed = server.sendmail(From, to, msg.as_string())
    server.quit()

  def prepareMail(self, From, to, subject, attachments):
    msg = MIMEMultipart()
    msg['From'] = From
    msg['To'] = to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    # The Body message is empty
    msg.attach( MIMEText("") )

    for file in attachments:
      #We could check for mimetypes here, but I'm too lazy
      part = MIMEBase('application', "octet-stream")
      part.set_payload( open(file,"rb").read() )
      Encoders.encode_base64(part)
      part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
      msg.attach(part)
      #Delete created Tar
    return msg

if __name__ == '__main__':
  mail = SendMail()
  # Send all files included in command line arguments
  mail.send(sys.argv[1:])

server = smtplib.SMTP(self.smtpserver)
server.ehlo() #Has something to do with sending information
server.starttls() # Use encrypted SSL mode
server.ehlo() # To make starttls work
server.login(self.username, self.password)
