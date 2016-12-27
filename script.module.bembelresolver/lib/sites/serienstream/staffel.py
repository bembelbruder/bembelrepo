import help_fns

from sites.serienstream.folge import Folge

class Staffel:
    regexFolgen = '<td>(?P<nr>\d{1,2})</td>\n.*<td><a href="(?P<url>.*)">\n.*<strong>(?P<name>.*)</strong>'
    regexFolgen = 'Folge (?P<nr>\d*)\W*</a>\n\W*</td>\n\W*<td class="seasonEpisodeTitle">\n\W*<a href="(?P<url>[^"]*)">\n\W*<strong>(?P<name>[^<]*)</strong>'

    def init(self, url, img):
        self.url = url
        self.img = img
        
    def getParams(self):
        return {"url": self.url, "type": "staffel", "img": self.img}
    
    def getContent(self):
        res = []
        for m in help_fns.findAtUrl(self.regexFolgen, self.url):
            x = m.groupdict()
            newFolge = Folge()
            newFolge.name = x['nr'].zfill(2) + " - " + x['name']
            newFolge.url = x['url']
            newFolge.img = self.img
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
    
