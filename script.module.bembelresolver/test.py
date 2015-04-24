from hoster import vivo
from sites.filmpalast.filmpalast import Filmpalast
from sites.kinox.kinox import Kinox
from sites.kkiste.kkiste import KKiste
from sites.serien.staffel import Staffel
from hoster.FileNotExistsException import FileNotExistsException
from email.mime.text import MIMEText
import smtplib
import email.utils
import getpass

#print vivo.Vivo().getVideoUrl("http://vivo.sx/2f06e20a67")

def sendMail(text):
    msg = MIMEText(text)
    msg.set_unixfrom("Sascha Kronhart")
    msg['To'] = email.utils.formataddr(('Recipient', 'sascha.kronhart@gmail.com'))
    msg['From'] = email.utils.formataddr(('Sascha Kronhart', 'bembelkodi@mail.de'))
    msg['Subject'] = 'Test from bembelresolver'
    
    server = smtplib.SMTP_SSL("smtp.mail.de")
    try:
        server.ehlo()
        server.login("bembelkodi@mail.de", "E1ntracht")
        server.sendmail("bembelkodi@mail.de", "sascha.kronhart@gmail.com", msg.as_string())
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
        
s = Staffel()
s.url = "http://bs.to/serie/Navy-CIS/10"

fileNotFoundUrls = []
exceptionUrls = []

res = ""
counter = 0
for f in s.getContent():
    print f.url
    f.url = "http://bs.to/" + f.url
    if counter > 3 and counter < 5:
        f.displayName = "test"
        for h in f.getContent():
            h.hoster = h.name
            h.url = "http://bs.to/" + h.url
            
            try:
                h.getVideoUrl()
            except FileNotExistsException:
                res += "Folgende url wird nicht gefunden: " + h.url + "\n"
                fileNotFoundUrls.append(h.url)
            except:
                res += "Folgende url verursacht einen Fehler: " + h.url + "\n"
                exceptionUrls.append(h.url)
    counter += 1

sendMail(res)
#fp.searchFilm()
#fp.showFilm("http://kkiste.to/exodus-stream.html", "Godzilla")
#fp.showHoster("http://kinox.to/aGET/Mirror/Exodus-1&Hoster=30&Mirror=1", "StreamCloud.eu", "Godzilla")
#fp.showPart("http://www.ecostream.tv/stream/50cb20989bd2ad5cca9a540b1f21cb1b.html", "Ecostream", "Godzilla")
#fp.showVideoByUrl('http://www.ecostream.tv/stream/c56825c124058745f3b36cc0212c0e27.html', "Ecostream", "Godzilla")

