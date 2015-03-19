import help_fns
import re
import urllib
import time

class Vivo:
	def getVideoUrl(self, pUrl):
		link = help_fns.openUrl(pUrl)
	
		myhash = re.compile('name="hash" value="([^"]*)"').findall(link)[0]
		timestamp = re.compile('name="timestamp" value="([^"]*)"').findall(link)[0]
		data = {"hash": myhash, "timestamp": timestamp}
		data = urllib.urlencode(data)	
	
		time.sleep(7)
	
		print data
		link = help_fns.openUrlWithData(pUrl, data)
	
		url = re.compile('data-url="([^"]*)"').findall(link)[0]
		return url
	
	def getVideoUrl_Outside(self, url):
		return self.getVideoUrl(self.getInnerUrl(url))
	
	def getInnerUrl(self, url):
		return help_fns.findAtUrl("href='(http://vivo.sx[^']*)'", url)[0]	
	
	def getDownloadCommand(self):
		return ""