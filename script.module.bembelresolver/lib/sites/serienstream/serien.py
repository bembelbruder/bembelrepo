import help_fns
import re

from sites.serienstream.serie import Serie

class Serien:
    img = ""
    regexSerien = '<a href="(?P<url>[^"]*)" title="[^"]*"> <img src="(?P<img>[^"]*)" [^<]*<h3>(?P<name>[^<]*)'
    
    def init(self, url):
        self.url = url
    
    def getParams(self):
        return {"url": self.url, "type": "serien"}

    def getContent(self):
        res = []

        print self.url
        match = help_fns.findAtUrl(self.regexSerien, self.url)        
        for m in match:
            x = m.groupdict()
            newSerie = Serie()
            newSerie.name = x['name']
            newSerie.url = x['url']
            newSerie.img = "http://serienstream.to/" + x['img']
            res.append(newSerie)
            
        return res

    def isDownloadable(self):
        return False

