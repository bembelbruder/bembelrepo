import help_fns

from sites.serien.folge import Folge

class Staffel:
    regexFolgen = '<td>(?P<nr>\d{1,2})</td>\n.*<td><a href="(?P<url>.*)">\n.*<strong>(?P<name>.*)</strong>'

    def init(self, url):
        self.url = url
        
    def getParams(self):
        return {"url": self.url, "type": "staffel"}
    
    def getContent(self):
        res = []
        for m in help_fns.findAtUrl(self.regexFolgen, self.url):
            x = m.groupdict()
            newFolge = Folge()
            newFolge.name = x['nr'].zfill(2) + " - " + x['name']
            newFolge.url = x['url']
            res.append(newFolge)
            
        return res
    
    def getFolge(self, folge):
        res = self.getContent()
        
        for f in res:
            if f.name.startswith(str(folge).zfill(2)):
                return f
            
        return None
    
    def isDownloadable(self):
        return False
    
