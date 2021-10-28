import smtplib, ssl
import os
from optparse import OptionParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#variaveis configuráveis
from wordpass import senha, user, ports, hosts, destinatario

#variaveis de menu
from var import processar_resposta

#config smtp
host = hosts
port = ports
login = user
password = senha

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(login, password)

#Construção do email
message ='0'
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = destinatario
email_msg['Subject'] = processar_resposta()

server.quit()
