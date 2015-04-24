import help_fns
import re
import urllib

from hoster.BaseHoster import BaseHoster

class Videoweed(BaseHoster):
	regexInnerUrl = 'href="(http://videoweed.es[^"]*)"'

	def getVideoUrl(self, url):
		link = help_fns.openUrl(url)
	
		cid = re.compile('cid="([^"]*)"').findall(link)[0]
		key = re.compile('key="([^"]*)"').findall(link)[0]
		myfile = re.compile('file="([^"]*)"').findall(link)[0]
	
		data = {"cid": cid, "file": myfile, "key": key}
		data = urllib.urlencode(data)
	
		match = help_fns.findAtUrl("url=([^&]*)", "http://www.videoweed.es/api/player.api.php?" + data)
	
		return match[0]
	
	def getDownloadCommand(self):
		return ""