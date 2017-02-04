import help_fns
from urllib import urlretrieve
import urllib2
import os
from os.path import expanduser
import requests


class Hoster:
    
    def init(self, url, hoster, displayName):
        self.url = url
        self.hoster = hoster
        self.displayName = displayName
    
    def getParams(self):
        return {"url": self.url, "type": "hoster", "displayName": self.displayName, "hoster": self.name}
        
    def getVideoUrl(self):
        regexInnerUrl = "https://bs.to/out/\d*"
        self.url = help_fns.findAtUrlAsGroup(regexInnerUrl, self.url)[0]
        self.url = self.getFinalUrl(self.url)

        return help_fns.knownHosts[self.hoster].getVideoUrl(self.url)
    
    def getImage(self):
        return ""
        #return "https:" + help_fns.findAtUrl('<img src="(//s.burning-seri.es/img/cover/[^"]*)" alt="Cover"/>', self.url)[0]

    def isDownloadable(self):
        return True

    def download(self):
        fileUrl = self.getVideoUrl()
        print fileUrl
        filename, fileExtension = os.path.splitext(fileUrl)
        if fileExtension == "":
            fileExtension = ".mp4"

        urlretrieve(fileUrl, expanduser("~/Videos/" + self.displayName + fileExtension))
        
    def getFinalUrl(self, url):
        r = requests.get(url)
        return r.url
