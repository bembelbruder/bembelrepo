import help_fns

from sites.serien.hoster import Hoster

class Folge:
    regexHoster = 'href="(.*)"><span\n\W*class="icon (.*)"></span> (.*) - Teil 1</a>'

    def init(self, url, displayName):
        self.url = url
        self.displayName = displayName
        
    def getParams(self):
        return {"url": self.url, "type": "folge", "displayName": self.name}
    
    def getContent(self):
        res = []
        for m in help_fns.findAtUrl(self.regexHoster, self.url):
            newHoster = Hoster()
            newHoster.name = m[2]
            newHoster.url = m[0]
            newHoster.displayName = self.displayName
            
            if newHoster.name in help_fns.knownHosts:
                res.append(newHoster)
                
            
        return res
    
    def isDownloadable(self):
        return False
    
