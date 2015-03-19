import urllib
import help_fns
import re
import cookielib
import urllib2
import time

class Youwatch:
	def getValue(self, name, link):
		regex = '"' + name + '" value="([^"]*)"' 
		return re.compile(regex).findall(link)[0]
	
	def getVideoUrl(self, url):
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	
		link = opener.open(url).read()
	
		op = "download1" # getValue('op', link)
		usr_login = self.getValue('usr_login', link)
		fname = self.getValue('fname', link)
		referer = self.getValue('referer', link)
		imhuman = self.getValue('imhuman', link)
		method_premium = self.getValue('method_premium', link)
	
		data = {'op': op, 'usr_login': usr_login, 'id': id, 'fname': fname, 'referer': referer, 'hash': hash, 'imhuman': imhuman, 'method_premium': method_premium}
	
		data = urllib.urlencode(data)
		time.sleep(11)
	
		link = opener.open(url, data).read()
		match = re.compile("video\\|([^|]*)").findall(link)
	
		return "http://fs9.youwatch.org:8777/" + match[0] + "/video.mp4"
	
	def getVideoUrl_Outside(self, url):
		return self.getVideoUrl(help_fns.findAtUrl("href='(http://youwatch.org/[^']*)'", url)[0])
	
	def getDownloadCommand(self):
		return ""