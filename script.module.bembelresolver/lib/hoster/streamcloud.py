import cookielib
import urllib2
import urllib
import re
import time
import help_fns

from hoster.FileNotExistsException import FileNotExistsException
from hoster.BaseHoster import BaseHoster

class Streamcloud(BaseHoster):
	regexStreamcloudMP4 = '<input type="hidden" name="op" value="(.*)">\n\W*<input type="hidden" name="usr_login" value="">\n\W*<input type="hidden" name="id" value="(.*)">\n\W*<input type="hidden" name="fname" value="(.*)">\n\W*<input type="hidden" name="referer" value="(.*)">\n\W*<input type="hidden" name="hash" value="">\n\W*<input type="submit" name="imhuman" id="btn_download" class="button gray" value="(.*)">'
	regexStreamcloudFile = 'file: "(.*\.(mp4|flv))"'
	regexInnerUrl = 'href="(http://streamcloud[^"]*)"'
	
	def getVideoUrlByOutsideLink(self, link):
		tmp = re.compile(self.regexInnerUrl).findall(link)[0]
		return self.getVideoUrl(tmp)
	
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
		print url
		print data
		link = opener.open(url, data).read()
	
		match = re.compile(self.regexStreamcloudFile).findall(link)
		return match[0][0]
		
	def isFileNotExists(self, link):
		match = re.compile("File Not Found").findall(link)
		if match:
			return True
		else:
			return False
	
	def getDownloadCommand(self):
		return ""