import sys
from os.path import expanduser
sys.path.append(expanduser("~/.kodi/addons/script.module.bembelresolver/lib"))

from sites.serien.serie import Serie
import ConfigParser
import email.utils
from email.mime.text import MIMEText
import smtplib

class FinderBean:
    url = ""
    staff = ""
    number = ""
    
def exists(serie, staffel, number):
    s = serie.getStaffel(staffel)

    if s != None:
        f = s.getFolge(number)
        return f != None
    else:
        return False

def sendMail(text):
    config = ConfigParser.RawConfigParser()
    config.read(expanduser("~/mailConfig.cfg"))
    
    recipient = config.get("Mail", "recipient")
    sender = config.get("Mail", "sender")
    senderName = config.get("Mail", "senderName")
    password = config.get("Mail", "password")
    smtpServer = config.get("Mail", "smtpServer")
    
    msg = MIMEText(text)
    msg.set_unixfrom(senderName)
    msg['To'] = email.utils.formataddr(('Recipient', recipient))
    msg['From'] = email.utils.formataddr((senderName, sender))
    msg['Subject'] = 'Neues zum Gucken'
    
    server = smtplib.SMTP_SSL(smtpServer)
    try:
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
    finally:
        server.quit()

finderBeans = []

config = ConfigParser.RawConfigParser()
config.read(expanduser("~/serien.cfg"))

emailText = ""
for sec in config.sections():
    s = Serie()
    s.init(config.get(sec, "url"))
    
    staffel = config.getint(sec, "staffel")
    folge = config.getint(sec, "folge")

    if exists(s, staffel, folge + 1):
        emailText += "Neue Folge gefunden fuer " + sec + " (Staffel " + str(staffel) + ", Folge " + str(folge  + 1) + ")\n"
        config.set(sec, "folge", folge + 1)
    else:
        if exists(s, staffel + 1, 1):
            emailText += "Neue Staffel gefunden fuer " + sec + " (Staffel " + str(staffel) + ", Folge 1)\n"
            config.set(sec, "staffel", staffel + 1)
            config.set(sec, "folge", 1)

if emailText != "":            
    with open(expanduser("~/serien.cfg"), 'wb') as configfile:
        config.write(configfile)
    sendMail(emailText)
