from sites.BaseSite import BaseSite

class Filmpalast(BaseSite):
	
	def __init__(self, dataProvider):
		BaseSite.__init__(self, dataProvider)
		self.searchUrl = "http://www.filmpalast.to/search/title/"
		self.searchRegex = '<a href="(?P<url>http://www.filmpalast.to/movies/view/[^"]*)" class="rb">(?P<name>.*)</a>'
		self.hosterRegex = 'class="hostName">(?P<hoster>.*)</p></li>(\\s*.*){4}_blank" href="(?P<url>[^"]*)"'
		
	def getName(self):
		return "Filmpalast"
	
	def showHoster(self, url, hosterName, displayName):
		self.showVideoByUrl(url, hosterName, displayName)
