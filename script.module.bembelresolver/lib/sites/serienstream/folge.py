import help_fns
import requests
import re

from sites.serienstream.hoster import Hoster

class Folge:
    regexHoster = '<a href="/(?P<url>[^"]*)" target="_blank">(\n.*){2}\n\W*<h4>(?P<name>[^"]*)</h4>'

    def init(self, url, displayName, img):
        self.url = url
        self.displayName = displayName
        self.img = img
        
    def getParams(self):
        print "Image: " + self.img
        return {"url": self.url, "type": "folge", "displayName": self.name, "img": self.img}
    
    def getContent(self):
        res = []
        
        r = requests.get(self.url)

        for m in re.compile(self.regexHoster).finditer(r.text):
            x = m.groupdict()
            newHoster = Hoster()
            newHoster.name = x['name']
            newHoster.url = x['url']
            newHoster.displayName = self.displayName
            newHoster.img = self.img
            
            if newHoster.name in help_fns.knownHosts:
                res.append(newHoster)
                
            
        return res
    
    def download(self):
        hoster = self.getContent()
        res = self.tryDownloadHoster(hoster, "Streamcloud")
        if not res:
            res = self.tryDownloadHoster(hoster, "Vivo")
        if not res:
            res = self.tryDownloadHoster(hoster, "Vidto")
        if not res:
            res = self.tryDownloadHoster(hoster, 'Powerwatch')
                
    def tryDownloadHoster(self, allHoster, hoster):
        try:
            for h in allHoster:
                if h.name == hoster:
                    h.hoster = hoster
                    h.url = "http://bs.to/" + h.url
                    h.displayName = self.displayName
                    h.download()
                    return True
        except:
            return False
            
        return False
    
    def getUnknowHoster(self):
        res = []
        
        for m in help_fns.findAtUrl(self.regexHoster, self.url):
            x = m.groupdict()
            newHoster = Hoster()
            newHoster.name = x['name']
            newHoster.url = x['url']
            newHoster.displayName = self.displayName
            
            if not newHoster.name in help_fns.knownHosts:
                res.append(newHoster)
    
        return res
    
    def isDownloadable(self):
        return False
    
