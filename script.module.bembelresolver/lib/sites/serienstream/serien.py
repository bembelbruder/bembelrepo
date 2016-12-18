import help_fns
import re

from sites.serienstream.serie import Serie

class Serien:
    regexSerien = '<a href="(?P<url>[^"]*)"(\n.*){6}<h3>(?P<name>[^<]*)<span'
    
    def init(self, url):
        self.url = url
    
    def getParams(self):
        return {"url": self.url, "type": "serien"}

    def getContent(self):
        res = []

        match = help_fns.findAtUrl(self.regexSerien, self.url)        
        for m in match:
            x = m.groupdict()
            newSerie = Serie()
            newSerie.name = x['name']
            newSerie.url = x['url']
            res.append(newSerie)
            
        return res

    def isDownloadable(self):
        return False

