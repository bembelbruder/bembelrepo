import help_fns
import urllib
import re
from hoster.FileNotExistsException import FileNotExistsException

class BaseSite:
	
	def __init__(self, dataProvider):
		self.dataProvider = dataProvider
	
	def showFilm(self, url, displayName):
		link = help_fns.openUrl(url)
		
		res = self.getHostsByFilm(link, displayName)
		
		self.dataProvider.printResult(res)
	
	def showVideoByUrl(self, url, hosterName, displayName):
		link = help_fns.openUrl(url)
		self.showVideoByLink(link, hosterName, displayName)
	
	def showVideoByLink(self, link, hosterName, displayName):
		try:
			videoUrl = self.getLinkByHostLink(link, hosterName)
			self.dataProvider.handleVideoLink(videoUrl, displayName)
		except FileNotExistsException:
			self.dataProvider.handleFileNotExistsException()
		
	
	def showHoster(self, url, hosterName, displayName):
		link = help_fns.openUrl(url)
		
		parts = self.getParts(link, hosterName, displayName)
		if len(parts) == 0:
			self.showVideoByLink(link, hosterName, displayName)
		else:
			self.dataProvider.printResult(parts)

	def searchFilm(self):
		url = self.searchUrl + self.dataProvider.getSearchString()
		res = []
		match = help_fns.findAtUrl(self.searchRegex, url)
		for r in match:
			newItem = ResultBean()
			newItem.name = r[1]
			newItem.params = {"urlFilm": r[0], "displayName": r[1]} 
			res.append(newItem)
		
		self.dataProvider.printResult(res)

	def getParts(self, link, hoster, displayName):
		match = re.compile(self.partsRegex).findall(link)

		res = []
		for m in match:
			newItem = ResultBean()
			newItem.name = "Teil " + m[1]
			newItem.params = {'urlPart': m[0], "hoster": hoster, "displayName": displayName}
			res.append(newItem)
			
		return res
	
	def getHostsByFilm(self, pUrl, pDisplayName):
		res = []
		match = help_fns.findAtUrl(self.hosterRegex, pUrl)

		for m in match:
			if m[0] in help_fns.knownHosts:
				newItem = ResultBean()
				newItem.name = m[0]
				newItem.params = {"urlHoster": m[2], "hoster": m[0], "displayName": pDisplayName}
				res.append(newItem)

		return res
	
	def getLinkByHostLink(self, pLink, pHoster):
		if pHoster in help_fns.knownHosts:
			return help_fns.knownHosts[pHoster].getVideoUrlByOutsideLink(pLink)

	def handleParameter(self, params):
		urlFilm = urllib.unquote(str(params.get("urlFilm", "")))
		urlHoster = urllib.unquote(str(params.get("urlHoster", "")))
		urlPart = urllib.unquote(str(params.get("urlPart")))
		displayName = urllib.unquote(str(params.get("displayName", "")))
		hosterName = urllib.unquote(str(params.get("hoster", "")))
	
		if urlFilm:
			self.showFilm(urlFilm, displayName)
		elif urlHoster:
			self.showHoster(urlHoster, hosterName, displayName)
		elif urlPart:
			self.showVideoByUrl(urlPart, hosterName, displayName)
		else:
			self.searchFilm()

class ResultBean:
	name = ""
	params = {}
