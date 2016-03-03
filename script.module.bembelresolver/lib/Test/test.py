import sys
from os.path import expanduser
from lib.sites.cine.cine import Cine
import help_fns
import urllib
from lib.sites.serien.serie import Serie
from lib.sites.serien.folge import Folge
from lib.hoster.streamcloud import Streamcloud
from urllib import urlretrieve
sys.path.append(expanduser("~/.kodi/addons/script.module.bembelresolver/lib"))

from sites.serien.staffel import Staffel
from sites.serien.hoster import Hoster
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
        return "fack ju"
    
    def printResult(self, res):
        for r in res:
            print r.name + " " + r.params["url"]
            
    def handleVideoLink(self, url, name):
        print "Spiele Video: " + url

# hosterCollector = HosterCollector.HosterCollector()      
# s = Staffel()
# s.url = "http://bs.to/serie/Navy-CIS/10"
#   
# res = ""
# counter = 0
# for f in s.getContent():
#     print f.url
#     f.url = "http://bs.to/" + f.url
#     f.displayName = "test"
#     for h in f.getContent():
#         h.url = "http://bs.to/" + h.url
#         h.hoster = h.name
#           
#         try:
#             h.getVideoUrl()
#             hosterCollector.addHoster(h.name, h.url, 1)
#         except FileNotExistsException:
#             hosterCollector.addHoster(h.name, h.url, 2)
#         except:
#             hosterCollector.addHoster(h.name, h.url, 3)
#     
#     for h in f.getUnknowHoster():
#         hosterCollector.addHoster(h.name, h.url, 4)
# sendMail(hosterCollector.getText())
provider = TestDataProvider()
fp = Cine(provider)
fp.searchFilm()
data = (('ID', '3702996'), ('lang', 'de'))
data = urllib.urlencode(data)
print help_fns.openUrl("http://cine.to/out/85749")
#fp.showHoster("http://kinox.to/aGET/Mirror/Exodus-1&Hoster=30&Mirror=1", "StreamCloud.eu", "Godzilla")
#fp.showPart("http://www.ecostream.tv/stream/50cb20989bd2ad5cca9a540b1f21cb1b.html", "Ecostream", "Godzilla")
#fp.showVideoByUrl('http://www.ecostream.tv/stream/c56825c124058745f3b36cc0212c0e27.html', "Ecostream", "Godzilla")

# links = ["http://streamcloud.eu/yyq7hpmuhxia/Bibi_und_Tina_-_S01E02_-_Sabrinas_Fohlen.avi.html",
# "http://streamcloud.eu/r3p5z97c59fj/Bibi_und_Tina_-_S01E03_-_Die_Wildpferde.mp4.mp4.html",
# "http://streamcloud.eu/gj3k32ycftzl/Bibi_und_Tina_-_S01E04_-_Der_verhexte_Sattel.avi.html",
# "http://streamcloud.eu/5x4rzz01mlw6/Bibi_und_Tina_-_S01E05_-_Der_Liebesbrief.avi.html",
# "http://streamcloud.eu/l8yc119sckvs/Bibi_und_Tina_-_S01E06_-_Alex_und_das_Internat.avi.html",
# "http://streamcloud.eu/okpnjlx6ssyx/Bibi_und_Tina_-_S02E01_-_Das_Gespensterpferd.avi.html",
# "http://streamcloud.eu/hfbccduvofrf/Bibi_und_Tina_-_S02E02_-_Tina_in_Gefahr.avi.html",
# "http://streamcloud.eu/h7w1s5yjacwj/Bibi_und_Tina_-_S02E03_-_Die_Pferde_sind_krank.avi.html",
# "http://streamcloud.eu/8qnrc9ps0yeu/Bibi_und_Tina_-_S02E04_-_Papi_lernt_reiten.avi.html",
# "http://streamcloud.eu/j8btkc1svcbq/Bibi_und_Tina_-_S02E05_-_Ein_Pony_zum_Knuddeln.avi.html",
# "http://streamcloud.eu/t9a8xcti9opg/Bibi_und_Tina_-_S02E06_-_Der_Hufschmied.avi.html",
# "http://streamcloud.eu/t9a8xcti9opg/Bibi_und_Tina_-_S02E06_-_Der_Hufschmied.avi.html"]
# 
# sc = Streamcloud()
# counter = 2
# for link in links:
#     urlretrieve(sc.getVideoUrl(link), "/home/sascha/bibiundtina/staffel1/file_" + str(counter))
#     print "Datei " + str(counter) + " fertig"
#     counter += 1
# 
# staffel2 = ["http://streamcloud.eu/urn1nspx0lbj/Bibi_und_Tina_-_S03E01_-_Die_geheimnisvolle_Statue.avi.html",
#             "http://streamcloud.eu/9b8a5gzbfek0/Bibi_und_Tina_-_S03E02_-_Der_Hundedieb.avi.html",
#             "http://streamcloud.eu/bqtm0p9w1yiu/Bibi_und_Tina_-_S03E03_-_Die_Schmugglerpferde.avi.html",
#             "http://streamcloud.eu/axokeg2zlz3c/Bibi_und_Tina_-_S03E04_-_Das_Schlossfest.avi.html",
#             "http://streamcloud.eu/euhubqutrmuw/Bibi_und_Tina_-_S03E05_-_Abenteuer_in_der_Burgruine.avi.html",
#             "http://streamcloud.eu/zhogsmgw5b8j/Bibi_und_Tina_-_S03E06_-_Sabrina_wird_entfuehrt.avi.html",
#             "http://streamcloud.eu/vnxoanj53vy4/Bibi_und_Tina_-_S03E07_-_Ein_Preis_fuer_den_Martinshof.avi.html",
#             "http://streamcloud.eu/lmg0e7j9bw88/Bibi_und_Tina_-_S03E08_-_Das_Westernturnier.avi.html",
#             "http://streamcloud.eu/1hj14b7jkztx/Bibi_und_Tina_-_S03E09_-_Das_grosse_Wettreiten.avi.html",
#             "http://streamcloud.eu/32rkqc9r9xlb/Bibi_und_Tina_-_S03E10_-_Das_Pferd_in_der_Schule.avi.html",
#             "http://streamcloud.eu/t2ew3z13vkad/Bibi_und_Tina_-_S03E11_-_Der_Pferdefluesterer.avi.html",
#             "http://streamcloud.eu/wg5zxf9ocvrj/Bibi_und_Tina_-_S03E12_-_Felix_der_Filmstar.avi.html",
#             "http://streamcloud.eu/7fl0w95aoxgd/Bibi_und_Tina_-_S03E13_-_Ein_unfaires_Rennen.avi.html"]
# 
# staffel3 = ["http://streamcloud.eu/9rhie7p4ah8j/Bibi_und_Tina_-_S04E01_-_Spuk_auf_der_Ferieninsel.avi.html",
#             "http://streamcloud.eu/pww79tym0auo/Bibi_und_Tina_-_S04E02_-_Nadja_und_Nafari.avi.html",
#             "http://streamcloud.eu/whd7ld3y0g1u/Bibi_und_Tina_-_S04E03_-_Das_zottelige_Trio.avi.html",
#             ""]