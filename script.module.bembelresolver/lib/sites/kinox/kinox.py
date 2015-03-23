from lib.sites.BaseSite import BaseSite

class Kinox(BaseSite):
	
	def __init__(self, dataProvider):
		self.dataProvider = dataProvider
		self.searchUrl = "http://kinox.to/Search.html?q="
		self.searchRegex = 'src="/gr/sys/lng/(\\d)\.png" alt="language"></td>\\n\\s*<td.*</td>\\n\\s*<td class="Title"><a href="([^"]*)" onclick="return false;">([^"]*)</a> <span class="Year">(\\d{4})'
		self.hosterRegex = 'rel="([^"]*)">\s<div class="Named">([^>]*)</div>'  
		self.partsRegex = '<a rel=\\\\"([^"]*)" class=\\\\"[^"]*">Part (\\d)'
		
	def getName(self):
		return "Kinox"