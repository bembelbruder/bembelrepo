import urllib
import help_fns

class Firedrive:
	def getVideoUrl(self, url):
		match = help_fns.findAtUrl('name="confirm" value="([^"]*)"', url)
		data = {'confirm': match[0]}
		data = urllib.urlencode(data)
	
		match = help_fns.findAtUrlWithData("file: '([^']*)'", url, data)
		return match[0]
	
	def getVideoUrl_Outside(self, url):
		match = help_fns.findAtUrl("href='(http://www.firedrive.com/file/[^']*)", url)
		
		return self.getVideoUrl(match[0])
	
	def getDownloadCommand(self):
		return ""