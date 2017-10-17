import help_fns
import re

from hoster.BaseHoster import BaseHoster

class RapidVideo(BaseHoster):
    regexInnerUrl = 'src="([^"]*)"'

    def getVideoUrl(self, url):
        print url
        link = help_fns.openUrl(url)
        match = re.compile('src="([^"]*)" type=').findall(link)
        
        print match[0]
        return match[0]