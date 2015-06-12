import urllib
import re
import cookielib
import urllib2
import time

from hoster.FileNotExistsException import FileNotExistsException
from hoster.BaseHoster import BaseHoster

class Youwatch(BaseHoster):
	regexInnerUrl = 'href="(http://youwatch.org[^"]*)"'
	
	def getValue(self, name, link):
		regex = '"' + name + '" value="([^"]*)"' 
		return re.compile(regex).findall(link)[0]
	
	def getVideoUrl(self, url):
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	
		link = opener.open(url).read()
	
		if self.isFileNotExists(link):
			raise FileNotExistsException

		op = "download1" # getValue('op', link)
		usr_login = self.getValue('usr_login', link)
		fname = self.getValue('fname', link)
		referer = self.getValue('referer', link)
		imhuman = self.getValue('imhuman', link)
		method_premium = self.getValue('method_premium', link)
		myhash = self.getValue("hash", link)
		myid = self.getValue("id", link)
		
		data = {'op': op, 'usr_login': usr_login, 'id': myid, 'fname': fname, 'referer': referer, 'hash': myhash, 'imhuman': imhuman, 'method_premium': method_premium}
		data = urllib.urlencode(data)
		time.sleep(11)
	
		link = opener.open(url, data).read()
		match = re.compile("'([^']*)'.split").findall(link)
		match = match[0].split("|")

		return "http://" + match[95] + ".youwatch.org:" + match[94] + "/" + match[93] + "/" + match[92] + "." + match[91]
	
	def isFileNotExists(self, link):
		match = re.compile("File Not Found").findall(link)
		if match:
			return True
		else:
			return False
