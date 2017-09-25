import help_fns
import re
import urllib
import time
import cookielib
import urllib2
import ssl
import requests
#import requests

from hoster.BaseHoster import BaseHoster
from hoster.FileNotExistsException import FileNotExistsException

class Watchers(BaseHoster):
    regexInnerUrl = "href='(http://watchers.to/[^']*)'"
    
    def getVideoUrl(self, pUrl):
         headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'keep-alive',
                    'Host': 'vivo.sx',
                    'Referer': 'https://vivo.sx/7e5ef59c3b',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0'}
 
         with requests.Session() as s:
             link = s.get(pUrl).text
             
             print link
             
             if self.isFileNotExists(link):
                 raise FileNotExistsException
         
    
    def getDownloadCommand(self):
        return ""
    
    def isFileNotExists(self, link):
        match = re.compile("The requested file could not be found").findall(link)
        if match:
            return True
        else:
            return False