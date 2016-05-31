import help_fns
import re
import urllib
import time
import cookielib
import urllib2

from hoster.BaseHoster import BaseHoster
from hoster.FileNotExistsException import FileNotExistsException

class Vivo(BaseHoster):
	regexInnerUrl = "href='(http://vivo.sx/[^']*)'"

	def getVideoUrl(self, pUrl):
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

		headers = [('Accept', '*/*'), ('Accept-Encoding', 'none'), ('Accept-Language', 'de-de,de;q=0.8,en-us;q=0.5,en;q=0.3'), ('Cache-Control', 'no-cache'), ('Connection', 'keep-alive'), ('Content-Length', '0'), ('Host', 'www.ecostream.tv'), ('Pragma', 'no-cache'), ('Referer', pUrl), ('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:23.0) Gecko/20100101 Firefox/23.0'), ('X-Requested-With', 'XMLHttpRequest')]
		opener.addheaders = headers

		link = opener.open(pUrl).read()
		
		if self.isFileNotExists(link):
			raise FileNotExistsException
	
		myhash = re.compile('name="hash" value="([^"]*)"').findall(link)[0]
		timestamp = re.compile('name="timestamp" value="([^"]*)"').findall(link)[0]
		data = {"hash": myhash, "timestamp": timestamp, "throttle": "1"}
		data = urllib.urlencode(data)	

		print data
		print pUrl
		time.sleep(7)
	
		link = opener.open(pUrl, data).read()
	
		url = re.compile('data-url="([^"]*)"').findall(link)[0]
		return url
	
	def getDownloadCommand(self):
		return ""
	
	def isFileNotExists(self, link):
		match = re.compile("The requested file could not be found").findall(link)
		if match:
			return True
		else:
			return False
