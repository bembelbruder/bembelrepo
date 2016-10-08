import re
import help_fns

from hoster.BaseHoster import BaseHoster
from hoster import jsunpack

class Vidto(BaseHoster):
    regexInnerUrl = "href='(http://vidto.me/[^']*)'"

    def getVideoUrl(self, pUrl):
        mediaId = re.compile(".*/(.*)\.html").findall(pUrl)[0]
        pUrl = "http://vidto.me/embed-" + mediaId + ".html"
     
        link = help_fns.openUrl(pUrl)   
        jsData = jsunpack.unpack(link)
            
        max_label = 0
        stream_url = ''
        for match in re.finditer('label:\s*"(\d+)p"\s*,\s*file:\s*"([^"]+)', jsData):
            label, link = match.groups()
            if int(label) > max_label:
                stream_url = link
                max_label = int(label)
                
        return stream_url