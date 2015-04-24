import help_fns
import re
import urllib

from hoster.BaseHoster import BaseHoster

class Movshare(BaseHoster):
	def getVideoUrl(self, url):
		link = help_fns.openUrl(url)
	
		cid = re.compile('cid="([^"]*)"').findall(link)[0]
		cid2 = "undefined"
		cid3 = "bs.to"
		key = re.compile('key="([^"]*)"').findall(link)[0]
		myfile = re.compile('file="([^"]*)"').findall(link)[0]
	
		data = {"cid": cid, "cid2": cid2, "cid3": cid3, "file": myfile, "filekey": key, "numOfErrors": "0", "pass": "undefined", "user": "undefined"}
		data = urllib.urlencode(data)
		link = help_fns.openUrl("http://www.movshare.net/api/player.api.php?" + data)
		print link
		match = help_fns.findAtUrl("url=([^&]*)", "http://www.movshare.net/api/player.api.php?" + data)
		print match
		return match[0]
	
	def getVideoUrl_Outside(self, url):
		match = help_fns.findAtUrl('href="(http://www.movshare.net/[^"]*)"', url)
		print match
		return self.getVideoUrl(match[0])
	
	def getDownloadCommand(self):
		return ""