from lib.sites.BaseSite import BaseSite

class KKiste(BaseSite):
	
	def __init__(self, dataProvider):
		self.dataProvider = dataProvider
		self.searchUrl = "http://kkiste.to/search/?q="
		self.searchRegex = '<a href="([^"]*)" title="[^"]*" class="title">([^<]*)</a>'
		self.hosterRegex = 'href="(http://www.ecostream.tv[^"]*)" target="_blank">Ecostream <small>.(.*)\]'
	
	def getName(self):
		return "KKiste"
