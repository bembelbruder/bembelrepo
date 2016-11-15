import help_fns
import urllib
import time
import re

from hoster.BaseHoster import BaseHoster

class Powerwatch(BaseHoster):
    regexInnerUrl = 'href="(http://powerwatch[^"]*)"'
    
    def getName(self, link, name):
        return re.compile('name="' + name + '" value="([^"]*)"').findall(link)[0]

    def getVideoUrl(self, url):
        link = help_fns.openUrl(url)
        url = re.compile("action='(http://powerwatch.pw/[^']*)").findall(link)[0]
        op = self.getName(link, 'op')
        usr_login = self.getName(link, 'usr_login')
        myid = self.getName(link, 'id')
        fname = self.getName(link, 'fname')
        referer = self.getName(link, 'referer')
        myhash = self.getName(link, 'hash')
        
        data = {'op': op,
                'usr_login': usr_login,
                'id': myid,
                'fname': fname,
                'referer': referer,
                'hash': myhash}
        print data
        data = urllib.urlencode(data)
        time.sleep(6)
        
        return help_fns.findAtUrlWithData('file:"([^"]*)"', url, data)[0]
        
    def getVideoUrl_Outside(self, url):
        return self.getVideoUrl(self.getInnerUrl(url))
    
    def getInnerUrl(self, url):
        return help_fns.findAtUrl(self.regexPowerwatch, url)[0]