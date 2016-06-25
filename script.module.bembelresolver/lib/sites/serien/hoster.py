import help_fns
from urllib import urlretrieve
import os
from os.path import expanduser


class Hoster:
    
    def init(self, url, hoster, displayName):
        self.url = url
        self.hoster = hoster
        self.displayName = displayName
    
    def getParams(self):
        return {"url": self.url, "type": "hoster", "displayName": self.displayName, "hoster": self.name}
        
    def getVideoUrl(self):
        return help_fns.knownHosts[self.hoster].getVideoUrl_ByOutsideUrl(self.url)
    
    def getImage(self):
        return ""
        #return "https:" + help_fns.findAtUrl('<img src="(//s.burning-seri.es/img/cover/[^"]*)" alt="Cover"/>', self.url)[0]

    def isDownloadable(self):
        return True

    def download(self):
        fileUrl = self.getVideoUrl()
        filename, fileExtension = os.path.splitext(fileUrl)
        if fileExtension == "":
            fileExtension = ".mp4"
            
        urlretrieve(self.getVideoUrl(), expanduser("~/Videos/" + self.displayName + fileExtension))