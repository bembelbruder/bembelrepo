import help_fns
import re

class BaseHoster:
    def getVideoUrl_ByOutsideLink(self, link):
        return self.getVideoUrl(self.getInnerUrlByLink(link))
        
    def getVideoUrl_ByOutsideUrl(self, url):
        return self.getVideoUrl(self.getInnerUrlByUrl(url))
    
    def getInnerUrlByLink(self, link):
        url = re.compile(self.regexInnerUrl).findall(link)[0]
        return url
    
    def getInnerUrlByUrl(self, url):
        link = help_fns.openUrl(url)
        return self.getInnerUrlByLink(link)