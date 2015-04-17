import help_fns
import re
import urllib
import time

from hoster.BaseHoster import BaseHoster
from hoster.FileNotExistsException import FileNotExistsException

class Vivo(BaseHoster):
	regexInnerUrl = "href='(http://vivo.sx/[^']*)'"

	def getVideoUrl(self, pUrl):
		link = help_fns.openUrl(pUrl)
		
		if self.isFileNotExists(link):
			raise FileNotExistsException
	
		myhash = re.compile('name="hash" value="([^"]*)"').findall(link)[0]
		timestamp = re.compile('name="timestamp" value="([^"]*)"').findall(link)[0]
		data = {"hash": myhash, "timestamp": timestamp}
		data = urllib.urlencode(data)	

		time.sleep(7)
	
		link = help_fns.openUrlWithData(pUrl, data)
	
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
