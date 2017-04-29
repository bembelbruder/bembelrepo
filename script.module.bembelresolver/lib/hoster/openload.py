import help_fns
from lib.hoster.BaseHoster import BaseHoster

class Openload(BaseHoster):
    
    def getVideoUrl(self, url):
        link = help_fns.openUrl(url)
        
        return link