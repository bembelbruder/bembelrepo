import help_fns

from sites.serien.staffel import Staffel

class Serie:
    regexStaffeln = '<li><a href="(?P<url>[^"]*)">(?P<name>\d*)</a></li>'

    def init(self, url):
        self.url = url
        
    def getParams(self):
        return {"url": self.url, "type": "serie"}
    
    def getContent(self):
        res = []
        print self.url
        for m in help_fns.findAtUrl(self.regexStaffeln, self.url):
            x = m.groupdict()
            newStaffel = Staffel()
            newStaffel.name = "Staffel " + x['name']
            newStaffel.url = x['url']
            res.append(newStaffel)
            
        return res
    
    def getStaffel(self, staffel):
        res = self.getContent()
        
        for s in res:
            if s.name == "Staffel " + str(staffel):
                s.url = "http://bs.to/" + s.url
                print s.url
                return s
            
        return None
    
    def isDownloadable(self):
        return False
    
