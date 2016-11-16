import help_fns
import re
import urllib2

class BaseHoster:
    def getVideoUrl_ByOutsideLink(self, link):
        return self.getVideoUrl(self.getInnerUrlByLink(link))
        
    def getVideoUrl_ByOutsideUrl(self, url):
        return self.getVideoUrl(self.getInnerUrlByUrl(url))
    
    def getInnerUrlByLink(self, link):
        regexInnerUrl = "https://bs.to/out/\d*"
        url = re.compile(regexInnerUrl).findall(link)[0]
        return self.getFinalUrl(url)
    
    def getInnerUrlByUrl(self, url):
        link = help_fns.openUrl(url)
        return self.getInnerUrlByLink(link)
    
    def getFinalUrl(self, url):
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        return res.geturl()
    
