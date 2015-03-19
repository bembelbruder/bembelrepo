import help_fns

from sites.serien.folge import Folge

class Staffel:
    regexFolgen = '<td>(\d{1,2})</td>\n.*<td><a href="(.*)">\n.*<strong>(.*)</strong>'

    def init(self, url):
        self.url = url
        
    def getParams(self):
        return {"url": self.url, "type": "staffel"}
    
    def getContent(self):
        res = []
        for m in help_fns.findAtUrl(self.regexFolgen, self.url):
            newFolge = Folge()
            newFolge.name = m[0] + " - " + m[2]
            newFolge.url = m[1]
            res.append(newFolge)
            
        return res
    
    def isDownloadable(self):
        return False
    
