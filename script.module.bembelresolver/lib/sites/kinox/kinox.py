from sites.BaseSite import BaseSite
import help_fns

class Kinox(BaseSite):
	
	def __init__(self, dataProvider):
		self.dataProvider = dataProvider
		self.searchUrl = "http://kinox.to/Search.html?q="
		self.searchResultPrefix = "http://kinox.to"
		self.searchRegex = 'src="/gr/sys/lng/(\\d)\.png" alt="language"></td>\\n\\s*<td.*</td>\\n\\s*<td class="Title"><a href="(?P<url>[^"]*)" onclick="return false;">(?P<name>[^"]*)</a> <span class="Year">(\\d{4})'
		self.hosterRegex = 'rel="(?P<url>[^"]*)">\s<div class="Named">(?P<hoster>[^>]*)</div>'  
		self.hosterResultPrefix = "http://kinox.to/aGET/Mirror/"
		self.partsRegex = '<a rel=\\\\"([^"]*)" class=\\\\"[^"]*">Part (\\d)'
		
	def getName(self):
		return "Kinox"
	
	def showHoster(self, url, hosterName, displayName):
		link = help_fns.openUrl(url)
		parts = self.getParts(link, hosterName, displayName)
		
		if len(parts) < 2:
			self.showVideoByLink(link, hosterName, displayName)
		else:
			self.dataProvider.printResult(parts)
