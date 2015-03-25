import urllib
import help_fns

from hoster.BaseHoster import BaseHoster

class Played(BaseHoster):
	regexPutlocker = '<a href="(http://www.putlocker.com/file/[^"]*)"' 
	regexPutlocker2 = '<input type="hidden" value="(.*)" name="fuck_you">'
	regexPlaylist = "playlist: '(.*)'"
	regexData = '<title>Video</title><media:content url="(.*\.flv)&amp;domain=putlocker.com" type="video/x-flv"'
	regexHash = 'name="hash" value="([^"]*)"'
	
	def getVideoUrl(self, url):
		match = help_fns.findAtUrl(self.regexHash, url)
	
		data = {'hash': match[0], 'imhuman': "Continue as Free User", 'op': 'download1', 'id': id}
		data = urllib.urlencode(data)
	
		link = help_fns.findAtUrlWithData('file: "([^"]*)"', url, data)
		return link[0]
	
	
	def getVideoUrl_Outside(self, url):
		match = help_fns.findAtUrl(self.regexPutlocker, url)
		
		return self.getVideoUrl(match[0])
	
	def getDownloadCommand(self):
		return ""