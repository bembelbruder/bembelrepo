import urllib
import re
import cookielib
import urllib2

class Vidstream:
	def getData(self, link, tag):
		match = re.compile('name="' + tag + '" value="([^"]*)"').findall(link)
		return match[0]
	
	
	def getVideoUrl(self, url):
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	
		link = opener.open(url).read()
		
		data = {'op': 'download1',
			'usr_login': self.getData(link, 'usr_login'),
			'id': self.getData(link, 'id'),
			'fname': self.getData(link, 'fname'),
			'referer': self.getData(link, 'referer'),
			'imhuman': 'Proceed to video',
			'hash': self.getData(link, 'hash')}
		data = urllib.urlencode(data)
	
		link = opener.open(url, data).read()
		match = re.compile('file: "([^"]*)"').findall(link)
		
		print match[0]
		return match[0]
	
	def getVideoUrl_Outside(self, url):
		return self.getVideoUrl("")
	
	def getDownloadCommand(self):
		return ""