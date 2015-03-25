import help_fns
import re
import urllib
import time

from hoster.BaseHoster import BaseHoster

class Vivo(BaseHoster):
	def getVideoUrl(self, pUrl):
		link = help_fns.openUrl(pUrl)
	
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