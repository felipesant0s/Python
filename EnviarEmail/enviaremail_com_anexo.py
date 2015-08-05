#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import csv

texto_msg = '''
Presado usuario(a) %(nome)s !!!

Este e um email enviado por um script PYTHON =D, seu email deve ficar aqui!!
'''

user = "seuemail@gmail.com"
pwd = "sua_senha"
anexo = "/home/felipe/teste.txt" #Caminho do anexo a ser enviado



def process(row, to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = user
   msg['To'] = row[0]
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach,'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(user, pwd)
   mailServer.sendmail(user, to, msg.as_string())
   mailServer.close()

if __name__ == '__main__':
  lista = open('/home/felipe/teste.csv') #Caminho da lista de email CSV
  csv_reader = csv.reader(lista)
  for row in csv_reader: 
      process(row, user,"Enviando Email com Python", texto_msg % {'nome':row[1]}, anexo)
  lista.close()