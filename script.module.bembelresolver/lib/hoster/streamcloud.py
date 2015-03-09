import cookielib
import urllib2
import urllib
import re
import time

import help_fns #@UnresolvedImport

regexStreamcloudMP4 = '<input type="hidden" name="op" value="(.*)">\n\W*<input type="hidden" name="usr_login" value="">\n\W*<input type="hidden" name="id" value="(.*)">\n\W*<input type="hidden" name="fname" value="(.*)">\n\W*<input type="hidden" name="referer" value="(.*)">\n\W*<input type="hidden" name="hash" value="">\n\W*<input type="submit" name="imhuman" id="btn_download" class="button gray" value="(.*)">'
regexStreamcloudFile = 'file: "(.*\.(mp4|flv))"'
regexBitshare = 'href="(http://streamcloud[^"]*)"'

def getVideoUrl(url):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	
	link = opener.open(url).read()
	dataMatch = re.compile(regexStreamcloudMP4).findall(link)
	data = {'op': dataMatch[0][0], 'usr_login': '', 'id': dataMatch[0][1], 'fname': dataMatch[0][2],
			'referer': '', 'hash': '', 'imhuman': dataMatch[0][4]}
	data = urllib.urlencode(data)

	time.sleep(11)
	link = opener.open(url, data).read()

	match = re.compile(regexStreamcloudFile).findall(link)
	return match[0][0]
	
def getVideoUrl_Outside(url):
	return getVideoUrl(getInnerUrl(url))

def getInnerUrl(url):
	return help_fns.findAtUrl(regexBitshare, url)[0]
