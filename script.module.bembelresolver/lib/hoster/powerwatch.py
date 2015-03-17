import help_fns
import urllib
import time

regexPowerwatch = 'href="(http://powerwatch[^"]*)"'

def getVideoUrl(url):
    regex = '<input type="hidden" name="op" value="(.*)">\n\W*<input type="hidden" name="usr_login" value="(.*)">\n\W*<input type="hidden" name="id" value="(.*)">\n\W*<input type="hidden" name="fname" value="(.*)">\n\W*<input type="hidden" name="referer" value="(.*)">\n\W*<input type="hidden" name="hash" value="(.*)">'
    
    dataMatch = help_fns.findAtUrl(regex, url)
    data = {'op': dataMatch[0][0], 'usr_login': dataMatch[0][1], 'id': dataMatch[0][2], 'fname': dataMatch[0][3],
            'referer': dataMatch[0][4], 'hash': dataMatch[0][5]}
    data = urllib.urlencode(data)
    
    time.sleep(6)
    
    return help_fns.findAtUrlWithData('file:"([^"]*)"', url, data)[0]
    
def getVideoUrl_Outside(url):
    return getVideoUrl(getInnerUrl(url))

def getInnerUrl(url):
    return help_fns.findAtUrl(regexPowerwatch, url)[0]