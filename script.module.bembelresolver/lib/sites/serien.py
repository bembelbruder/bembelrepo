from lib import help_fns

urlHost = "http://www.burning-seri.es/"

class Serien:
    regexSerien = '<li><a href="(serie/.*)">(.*)</a></li>'

    def getContent(self):
        res = []
        match = help_fns.findAtUrl(self.regexSerien, urlHost + "serie-alphabet")
        for m in match:
            newSerie = Serie()
            newSerie.name = m[1]
            newSerien.url = m[0]
            res.append(newSerie)
            
        return res
            
class Serie:
    regexStaffeln = '<li class=" (current)?"><a href="(.*)">(.*)</a></li>'

    def __init__(self):
        pass
    
    def __init__(self, url):
        self.url = url
        
    def getParams(self):
        return {"url": self.url, "type": "serie"}
    
    def getContent(self):
        res = []
        for m in help_fns.findAtUrl(self.regexStaffel, self.url):
            newStaffel = Staffel()
            newStaffel.name = "Staffel " + m[2]
            newStaffel.url = m[1]
            res.append(newStaffel)
            
        return res
    
    def isDownloadable(self):
        return False
    
class Staffel:
    regexFolgen = '<td>(\d{1,2})</td>\n.*<td><a href="(.*)">\n.*<strong>(.*)</strong>'

    def __init__(self):
        pass
    
    def __init__(self, url):
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
    
class Folge:
    regexHoster = 'href="(.*)"><span\n\W*class="icon (.*)"></span> (.*) - Teil 1</a>'

    def __init__(self):
        pass
    
    def __init__(self, url, displayName):
        self.url = url
        self.displayName = displayName
        
    def getParams(self):
        return {"url": self.url, type: "folge", "displayName": self.name}
    
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
    
class Hoster:
    def __init__(self):
        pass
    
    def __init__(self, url, hoster, displayName):
        self.url = url
        self.hoster = hoster
        self.displayName = displayName
    
    def getParams(self):
        return {"url": self.url, type: "hoster", "displayName": self.displayName, "hoster": self.name}
        
    def getVideoUrl(self):
        return help_fns.knownHosts[self.hoster].getVideoUrl_Outside(self.url)
    
    def getImage(self):
        return "https:" + help_fns.findAtUrl('<img src="(//s.burning-seri.es/img/cover/[^"]*)" alt="Cover"/>', hoster.url)[0]

    def isDownloadable(self):
        return True
