import help_fns
import re
import urllib2

class BaseHoster:
    def getVideoUrl_ByOutsideLink(self, link):
        return self.getVideoUrl(self.getInnerUrlByLink(link))
        
    def getVideoUrl_ByOutsideUrl(self, url):
        return self.getVideoUrl(self.getInnerUrlByUrl(url))
    
    def getInnerUrlByLink(self, link):
        return re.compile(self.regexInnerUrl).findall(link)[0]
    
    def getInnerUrlByUrl(self, url):
        link = help_fns.openUrl(url)
        return self.getInnerUrlByLink(link)
    
    
