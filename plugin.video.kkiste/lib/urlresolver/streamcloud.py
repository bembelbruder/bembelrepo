import cookielib
import urllib2
import urllib
import re
import time

from .. import help_fns

regexStreamcloudMP4 = '<input type="hidden" name="op" value="(.*)">\n\W*<input type="hidden" name="usr_login" value="">\n\W*<input type="hidden" name="id" value="(.*)">\n\W*<input type="hidden" name="fname" value="(.*)">\n\W*<input type="hidden" name="referer" value="(.*)">\n\W*<input type="hidden" name="hash" value="">\n\W*<input type="submit" name="imhuman" id="btn_download" class="button gray" value="(.*)">'
regexStreamcloudFile = 'file: "(.*\.mp4)"'
regexBitshare = 'href="(http://streamcloud[^"]*)"'

def getVideoUrl(url):
	print url
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
	return match[0]
	
def getVideoUrl_Outside(url):
	match = help_fns.findAtUrl(regexBitshare, url)

	return getVideoUrl(match[0])
