import help_fns

from sites.serien.hoster import Hoster

class Folge:
    regexHoster = '<li><a ( class="special")?href="(?P<url>[^"]*)">\n\W*<span class="icon [^1]*"></span>&nbsp;(?P<name>[\w]*)'

    def init(self, url, displayName):
        self.url = url
        self.displayName = displayName
        
    def getParams(self):
        return {"url": self.url, "type": "folge", "displayName": self.name}
    
    def getContent(self):
        res = []
        
        for m in help_fns.findAtUrl(self.regexHoster, self.url):
            x = m.groupdict()
            newHoster = Hoster()
            newHoster.name = x['name']
            newHoster.url = x['url']
            newHoster.displayName = self.displayName
            
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
    
