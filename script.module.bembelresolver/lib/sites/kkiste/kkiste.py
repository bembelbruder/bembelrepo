from lib.sites.BaseSite import BaseSite

class KKiste(BaseSite):
	
	def __init__(self, dataProvider):
		self.dataProvider = dataProvider
		self.searchUrl = "http://kkiste.to/search/?q="
		self.searchRegex = '<a href="(?P<url>[^"]*)" title="[^"]*" class="title">(?P<name>[^<]*)</a>'
		self.searchResultPrefix = "http://kkiste.to"
		self.partsRegex = 'href="(http://www.ecostream.tv[^"]*)" target="_blank">Ecostream <small>.(.*)\]'
		self.hosterRegex = 'href="(http://www.ecostream.tv[^"]*)" target="_blank">Ecostream <small>.(.*)\]'
	
	def getName(self):
		return "KKiste"

	def showFilm(self, url, displayName):
		self.showHoster(url, "Ecostream", displayName)
