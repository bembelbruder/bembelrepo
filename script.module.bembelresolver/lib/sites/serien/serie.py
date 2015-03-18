import help_fns

from sites.serien.staffel import Staffel

class Serie:
    regexStaffeln = '<li class=" (current)?"><a href="(.*)">(.*)</a></li>'

    def __init__(self, url):
        self.url = url
        
    def getParams(self):
        return {"url": self.url, "type": "serie"}
    
    def getContent(self):
        res = []
        for m in help_fns.findAtUrl(self.regexStaffel, self.url):
            newStaffel = Staffel
            newStaffel.name = "Staffel " + m[2]
            newStaffel.url = m[1]
            res.append(newStaffel)
            
        return res
    
    def isDownloadable(self):
        return False
    
