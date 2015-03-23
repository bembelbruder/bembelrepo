from lib.sites.BaseSite import BaseSite

class Filmpalast(BaseSite):
	
	def __init__(self, dataProvider):
		self.dataProvider = dataProvider
		self.searchUrl = "http://www.filmpalast.to/search/title/"
		self.searchRegex = '<a href="(http://www.filmpalast.to/movies/view/[^"]*)" class="rb">(.*)</a>'
		self.hosterRegex = 'class="hostName">(.*)</p></li>(\\s*.*){4}_blank" href="([^"]*)"'
		
	def getName(self):
		return "Filmpalast"