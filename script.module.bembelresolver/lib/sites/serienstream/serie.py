import help_fns

from sites.serienstream.staffel import Staffel

class Serie:
    regexStaffeln = '<a( class="active")? href="(?P<url>[^"]*)" title="(?P<name>Staffel [^"]*)">.*</a>'


    def init(self, url, img):
        self.url = url
        self.img = img
        
    def getParams(self):
        return {"url": self.url, "type": "serie", "img": self.img}
    
    def getContent(self):
        res = []
        for m in help_fns.findAtUrl(self.regexStaffeln, self.url):
            print self.img
            x = m.groupdict()
            newStaffel = Staffel()
            newStaffel.name = x['name']
            newStaffel.url = x['url']
            newStaffel.img = self.img
            res.append(newStaffel)
            
        return res
    
    def getStaffel(self, staffel):
        res = self.getContent()
        
        for s in res:
            if s.name == "Staffel " + str(staffel):
                s.url = "http://bs.to/" + s.url
                return s
            
        return None
    
    def isDownloadable(self):
        return False
    
