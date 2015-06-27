from hoster.BaseHoster import BaseHoster

import help_fns
import re
import urllib

class Shared(BaseHoster):
    regexInnerUrl = 'href="(http://shared[^"]*)"'

    def getVideoUrl(self, url):
        link = help_fns.openUrl(url)
        myhash = self.__getFormProperty(link, "hash")
        expires = self.__getFormProperty(link, "expires")
        timestamp = self.__getFormProperty(link, "timestamp")
        
        data = {"hash": myhash, "expires": expires, "timestamp": timestamp}
        data = urllib.urlencode(data)
        
        return help_fns.findAtUrlWithData('data-url="([^"]*)', url, data)[0]
    
    def __getFormProperty(self, link, name):
        return re.compile('<input type="hidden" name="' + name + '" value="([^"]*)"').findall(link)[0]