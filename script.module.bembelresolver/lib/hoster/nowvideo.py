import cookielib
import urllib2
import re
import help_fns

from hoster.BaseHoster import BaseHoster

class Nowvideo(BaseHoster):
	def getVideoUrl(self, url):
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	
		link = opener.open(url).read()
	
		key = re.compile('fkzd="([^"]*)"').findall(link)
		filename = re.compile('file="([^"]*)"').findall(link)
	
		url = "http://www.nowvideo.sx/api/player.api.php?"
		url += "file=" + filename[0]
		url += "&key=" + key[0]
		url += "&cid=1"
	
		link = help_fns.findAtUrl('url=([^&]*)', url)
		return link[0]
	
	def getDownloadCommand(self):
		return ""