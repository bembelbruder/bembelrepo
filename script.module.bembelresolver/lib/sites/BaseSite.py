import help_fns
import urllib
import re
from hoster.FileNotExistsException import FileNotExistsException

class BaseSite:
	
	def __init__(self, dataProvider):
		self.dataProvider = dataProvider
		self.searchResultPrefix = ""
		self.partsRegex = ""
	
	def showFilm(self, url, displayName):
		res = self.getHostsByFilm(url, displayName)
		
		self.dataProvider.printResult(res)
	
	def showVideoByUrl(self, url, hosterName, displayName):
		try:
			videoUrl = self.getLinkByHostUrl(url, hosterName)
			self.dataProvider.handleVideoLink(videoUrl, displayName)
		except FileNotExistsException:
			self.dataProvider.handleFileNotExistsException()
			
	def showVideoByLink(self, link, hosterName, displayName):
		url = help_fns.knownHosts[hosterName].getInnerUrlByLink(link)
		self.showVideoByUrl(url, hosterName, displayName)
	
	def showHoster(self, url, hosterName, displayName):
		link = help_fns.openUrl(url)
		
		parts = self.getParts(link, hosterName, displayName)
		if len(parts) < 2:
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
			newItem.params = {"url": self.searchResultPrefix + r[0], "displayName": r[1], "type": "film"} 
			res.append(newItem)
		
		self.dataProvider.printResult(res)

	def getParts(self, link, hoster, displayName):
		if self.partsRegex == "":
			return []
		
		match = re.compile(self.partsRegex).findall(link)

		res = []
		print match
		for m in match:
			newItem = ResultBean()
			newItem.name = m[1]
			newItem.params = {'url': m[0], "hoster": hoster, "displayName": displayName, "type": "part"}
			res.append(newItem)
			
		return res
	
	def getHostsByFilm(self, pUrl, pDisplayName):
		res = []
		match = help_fns.findAtUrl(self.hosterRegex, pUrl)
		
		for m in match:
			if m[0] in help_fns.knownHosts:
				newItem = ResultBean()
				newItem.name = m[0]
				newItem.params = {"url": m[2], "hoster": m[0], "displayName": pDisplayName, "type": "hoster"}
				res.append(newItem)

		return res
	
	def getLinkByHostUrl(self, url, hoster):
		if hoster in help_fns.knownHosts:
			return help_fns.knownHosts[hoster].getVideoUrl(url)
	
	def handleParameter(self, params):
		url = urllib.unquote(str(params.get("url")))
		urlType = urllib.unquote(str(params.get("type")))
		displayName = urllib.unquote(str(params.get("displayName", "")))
		hosterName = urllib.unquote(str(params.get("hoster", "")))
	
		if urlType == "film":
			self.showFilm(url, displayName)
		elif urlType == "hoster":
			self.showHoster(url, hosterName, displayName)
		elif urlType == "part":
			self.showVideoByUrl(url, hosterName, displayName)
		else:
			self.searchFilm()

class ResultBean:
	name = ""
	params = {}
