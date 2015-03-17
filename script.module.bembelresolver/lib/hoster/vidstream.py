import urllib
import re
import cookielib
import urllib2

def getData(link, tag):
	match = re.compile('name="' + tag + '" value="([^"]*)"').findall(link)
	return match[0]


def getVideoUrl(url):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	link = opener.open(url).read()
	
	data = {'op': 'download1',
		'usr_login': getData(link, 'usr_login'),
		'id': getData(link, 'id'),
		'fname': getData(link, 'fname'),
		'referer': getData(link, 'referer'),
		'imhuman': 'Proceed to video',
		'hash': getData(link, 'hash')}
	data = urllib.urlencode(data)

	link = opener.open(url, data).read()
	match = re.compile('file: "([^"]*)"').findall(link)
	
	print match[0]
	return match[0]

def getVideoUrl_Outside(url):
	return getVideoUrl("")

def getDownloadCommand():
	return ""