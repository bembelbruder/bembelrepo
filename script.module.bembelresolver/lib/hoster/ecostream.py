import re
import urllib
import urllib2
import cookielib
import help_fns

def getVideoUrl(url):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	headers = [('Accept', '*/*'), ('Accept-Encoding', 'none'), ('Accept-Language', 'de-de,de;q=0.8,en-us;q=0.5,en;q=0.3'), ('Cache-Control', 'no-cache'), ('Connection', 'keep-alive'), ('Content-Length', '0'), ('Host', 'www.ecostream.tv'), ('Pragma', 'no-cache'), ('Referer', url), ('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:23.0) Gecko/20100101 Firefox/23.0'), ('X-Requested-With', 'XMLHttpRequest')]

	opener.addheaders = headers

	tmpId = re.compile("http://www.ecostream.tv/stream/([^.]*)\\.html").findall(url)[0]
	link = opener.open(url).read()
	footerhash = re.compile("footerhash='([^']*)'").findall(link)[0]
	superslots = re.compile("superslots='([^']*)'").findall(link)[0]
	url = help_fns.findAtUrl("post\\('([^']*)'", "http://www.ecostream.tv/js/ecoss.js")[3]

	data = {'id': tmpId, 'tpm': footerhash + superslots}
	data = urllib.urlencode(data)

	print "http://www.ecostream.tv" + url 
	link = opener.open("http://www.ecostream.tv" + url , data).read()

	return "http://www.ecostream.tv" + re.compile('"url":"([^"]*)"').findall(link)[0]


def getVideoUrl_Outside(url):
	match = help_fns.findAtUrl("href='(http://www.ecostream.tv[^']*)'", url)

	return getVideoUrl(match[0])
