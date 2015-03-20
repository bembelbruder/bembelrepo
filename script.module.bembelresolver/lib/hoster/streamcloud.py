import cookielib
import urllib2
import urllib
import re
import time
import help_fns
from hoster.FileNotExistsException import FileNotExistsException

class Streamcloud:
	regexStreamcloudMP4 = '<input type="hidden" name="op" value="(.*)">\n\W*<input type="hidden" name="usr_login" value="">\n\W*<input type="hidden" name="id" value="(.*)">\n\W*<input type="hidden" name="fname" value="(.*)">\n\W*<input type="hidden" name="referer" value="(.*)">\n\W*<input type="hidden" name="hash" value="">\n\W*<input type="submit" name="imhuman" id="btn_download" class="button gray" value="(.*)">'
	regexStreamcloudFile = 'file: "(.*\.(mp4|flv))"'
	regexBitshare = 'href="(http://streamcloud[^"]*)"'
	
	def getVideoUrl(self, url):
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		
		link = opener.open(url).read()
		
		if self.isFileNotExists(link):
			raise FileNotExistsException
		
		dataMatch = re.compile(self.regexStreamcloudMP4).findall(link)
		data = {'op': dataMatch[0][0], 'usr_login': '', 'id': dataMatch[0][1], 'fname': dataMatch[0][2],
				'referer': '', 'hash': '', 'imhuman': dataMatch[0][4]}
		data = urllib.urlencode(data)
	
		time.sleep(11)
		link = opener.open(url, data).read()
	
		match = re.compile(self.regexStreamcloudFile).findall(link)
		return match[0][0]
		
	def isFileNotExists(self, link):
		match = re.compile("File Not Found").findall(link)
		if match:
			return True
		else:
			return False
		
	def getVideoUrl_Outside(self, url):
		return self.getVideoUrl(self.getInnerUrl(url))
	
	def getInnerUrl(self, url):
		return help_fns.findAtUrl(self.regexBitshare, url)[0]
	
	def getDownloadCommand(self):
		return ""