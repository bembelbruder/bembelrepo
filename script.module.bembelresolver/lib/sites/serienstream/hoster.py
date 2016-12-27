import help_fns
from urllib import urlretrieve
import urllib2
import os
import requests
from os.path import expanduser



class Hoster:
    
    def init(self, url, hoster, displayName, img):
        self.url = url
        self.hoster = hoster
        self.displayName = displayName
        self.img = img
    
    def getParams(self):
        return {"url": self.url, "type": "hoster", "displayName": self.displayName, "hoster": self.name, 'img': self.img}
        
    def getVideoUrl(self):
        self.url = self.getFinalUrl(self.url)
        return help_fns.knownHosts[self.hoster].getVideoUrl(self.url)
    
    def getImage(self):
        return self.img

    def isDownloadable(self):
        return True

    def download(self):
        fileUrl = self.getVideoUrl()
        filename, fileExtension = os.path.splitext(fileUrl)
        if fileExtension == "":
            fileExtension = ".mp4"
            
        urlretrieve(self.getVideoUrl(), expanduser("~/Videos/" + self.displayName + fileExtension))
        
    def getFinalUrl(self, url):
        r = requests.get(url)
        return r.url
