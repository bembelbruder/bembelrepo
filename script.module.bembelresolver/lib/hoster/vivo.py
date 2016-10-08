import help_fns
import re
import urllib
import time
import cookielib
import urllib2
import ssl
#import requests

from hoster.BaseHoster import BaseHoster
from hoster.FileNotExistsException import FileNotExistsException

class Vivo(BaseHoster):
	regexInnerUrl = "href='(http://vivo.sx/[^']*)'"

	def getVideoUrl(self, pUrl):
		print pUrl
		
# 		headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 				   'Accept-Encoding': 'gzip, deflate, br',
# 				   'Accept-Language': 'en-US,en;q=0.5',
# 				   'Connection': 'keep-alive',
# 				   'Host': 'vivo.sx',
# 				   'Referer': 'https://vivo.sx/7e5ef59c3b',
# 				   'Upgrade-Insecure-Requests': '1',
# 				   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0'}
# 
# 		with requests.Session() as s:
# 			print pUrl
# 			link = s.get(pUrl, headers = headers).text # opener.open(pUrl).read()
# 			
# 			if self.isFileNotExists(link):
# 				raise FileNotExistsException
# 		
# 			myhash = re.compile('name="hash" value="([^"]*)"').findall(link)[0]
# 			timestamp = re.compile('name="timestamp" value="([^"]*)"').findall(link)[0]
# 			data = {"hash": myhash, "timestamp": timestamp, "throttle": "1"}
# 			data = urllib.urlencode(data)	
# 	
# 			time.sleep(10)
# 				
# 			link = s.post(pUrl, data=data, headers = headers).content
# 			print link
# 			url = re.compile('data-url="([^"]*)"').findall(link)[0]
# 			return url
	
	def getDownloadCommand(self):
		return ""
	
	def isFileNotExists(self, link):
		match = re.compile("The requested file could not be found").findall(link)
		if match:
			return True
		else:
			return False
