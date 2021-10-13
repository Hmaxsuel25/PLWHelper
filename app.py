import os
import sys
import platform
import locale
import smtplib
import mimetypes
from optparse import OptionParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from wordpass import senha
from var import menu
from var import words

#config smtp
host = ""
port = ""
login = ""
password = senha

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(login, password)


#Construção
corpo = ""
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = ''
email_msg['Subject'] = menu

server.quit()
