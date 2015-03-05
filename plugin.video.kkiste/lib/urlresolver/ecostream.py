import re
import urllib
import urllib2
import cookielib

from .. import help_fns

def getVideoUrl(url):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	data = {'ss': '1', 'sss': '1'}
	data = urllib.urlencode(data)

	headers = [('Accept', '*/*'), ('Accept-Encoding', 'none'), ('Accept-Language', 'de-de,de;q=0.8,en-us;q=0.5,en;q=0.3'), ('Cache-Control', 'no-cache'), ('Connection', 'keep-alive'), ('Content-Length', '0'), ('Host', 'www.ecostream.tv'), ('Pragma', 'no-cache'), ('Referer', url), ('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:23.0) Gecko/20100101 Firefox/23.0'), ('X-Requested-With', 'XMLHttpRequest')]
	opener.addheaders = headers
	link = opener.open(url + "?ss=1", data).read()

	match = re.compile('data-id="([^"]*)"').findall(link)

	data = {'id': match[0]}
	data = urllib.urlencode(data)
	link = opener.open("http://www.ecostream.tv/xhr/video/get", data).read()
	
	match = re.compile('"url":"([^"]*)"').findall(link)
	return "http://www.ecostream.tv" + match[0]

def getVideoUrl_Outside(url):
	match = help_fns.findAtUrl("href=[\"'](http://www.ecostream.tv[^'\"]*)['\"]", url)

	return getVideoUrl(match[0])
