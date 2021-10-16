import smtplib
from optparse import OptionParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from wordpass import senha, user, ports, hosts
from var import menu, words

#config smtp
host = hosts
port = ports
login = user
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
