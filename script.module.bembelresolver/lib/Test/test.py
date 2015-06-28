import sys
from os.path import expanduser
sys.path.append(expanduser("~/.kodi/addons/script.module.bembelresolver/lib"))

from sites.serien.staffel import Staffel
from hoster.FileNotExistsException import FileNotExistsException
from email.mime.text import MIMEText
import smtplib
import email.utils
import ConfigParser
from Test import HosterCollector


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
    msg['Subject'] = 'Test from bembelresolver'
    
    server = smtplib.SMTP_SSL(smtpServer)
    try:
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
    finally:
        server.quit()
        
class TestDataProvider:
    def getSearchString(self):
        return "exodus"
    
    def printResult(self, res):
        for r in res:
            print r.name + " " + r.params["url"]
            
    def handleVideoLink(self, url, name):
        print "Spiele Video: " + url

hosterCollector = HosterCollector.HosterCollector()      
s = Staffel()
s.url = "http://bs.to/serie/Navy-CIS/10"
  
res = ""
counter = 0
for f in s.getContent():
    print f.url
    f.url = "http://bs.to/" + f.url
    f.displayName = "test"
    for h in f.getContent():
        h.url = "http://bs.to/" + h.url
        h.hoster = h.name
          
        try:
            h.getVideoUrl()
            hosterCollector.addHoster(h.name, h.url, 1)
        except FileNotExistsException:
            hosterCollector.addHoster(h.name, h.url, 2)
        except:
            hosterCollector.addHoster(h.name, h.url, 3)
    
    for h in f.getUnknowHoster():
        hosterCollector.addHoster(h.name, h.url, 4)
sendMail(hosterCollector.getText())
#fp.searchFilm()
#fp.showFilm("http://kkiste.to/exodus-stream.html", "Godzilla")
#fp.showHoster("http://kinox.to/aGET/Mirror/Exodus-1&Hoster=30&Mirror=1", "StreamCloud.eu", "Godzilla")
#fp.showPart("http://www.ecostream.tv/stream/50cb20989bd2ad5cca9a540b1f21cb1b.html", "Ecostream", "Godzilla")
#fp.showVideoByUrl('http://www.ecostream.tv/stream/c56825c124058745f3b36cc0212c0e27.html', "Ecostream", "Godzilla")

