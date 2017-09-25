import help_fns
import urllib
import re
from hoster.FileNotExistsException import FileNotExistsException

class BaseSite:
	
	def __init__(self, dataProvider):
		self.searchResultPrefix = ""
		self.dataProvider = dataProvider
		self.partsRegex = ""
		self.hosterResultPrefix = ""
	
	def showFilm(self, url, displayName):
		res = self.getHostsByFilm(url, displayName)
		
		self.dataProvider.printResult(res)
	
	def showStaffel(self, url, displayName, folgen, addr, seriesId, season):
		res = self.getEpisoden(url, displayName, folgen, addr, seriesId, season)
		
		self.dataProvider.printResult(res)

	def showHoster(self, url, hosterName, displayName):
		link = help_fns.openUrl(url)
		
		parts = self.getParts(link, hosterName, displayName)
		if len(parts) < 2:
			self.showVideoByLink(link, hosterName, displayName)
		else:
			self.dataProvider.printResult(parts)

	def showPart(self, url, hosterName, displayName):
		self.showVideoByUrl(url, hosterName, displayName)
		
	def showVideoByUrl(self, url, hosterName, displayName):
		try:
			videoUrl = self.getLinkByHostUrl(url, hosterName)
			self.dataProvider.handleVideoLink(videoUrl, displayName)
		except FileNotExistsException:
			self.dataProvider.handleFileNotExistsException()
			
	def showVideoByLink(self, link, hosterName, displayName):
		link = link.replace("\\", "")
		print link
		url = help_fns.knownHosts[hosterName].getInnerUrlByLink(link)
		self.showVideoByUrl(url, hosterName, displayName)
	
	def searchFilm(self):
		match = self.getSearchMatch()
		res = []
		for r in match:
			res.append(ResultBean(r["name"], {"url": self.searchResultPrefix + r["url"], "displayName": r["name"], "type": "film"}))
		
		self.dataProvider.printResult(res)
		
	def getSearchMatch(self):
		res = []
		url = self.searchUrl + self.dataProvider.getSearchString()
		match = help_fns.findAtUrl(self.searchRegex, url)
		for r in match:
			x = r.groupdict()
			res.append(x)
		
		return res
	
	def getParts(self, link, hoster, displayName):
		if self.partsRegex == "":
			return []
		
		match = re.compile(self.partsRegex).findall(link)

		res = []
		for m in match:
			res.append(ResultBean(m[1], {'url': m[0], "hoster": hoster, "displayName": displayName, "type": "part"}))
			
		return res
	
	def getEpisoden(self, pUrl, pDisplayName, pFolgen, addr, seriesId, season):
		print pFolgen
		res = []
		
		for f in pFolgen.split(","):
			res.append(ResultBean(f, {"url": pUrl, 
									  'displayName': pDisplayName,
									  'addr': addr,
									  'seriesId': seriesId,
									  'season': season, 
									  'episode': f, 
									  'type': 'episode'}))
			
		return res
	
	def getHostsByFilm(self, pUrl, pDisplayName):
		res = []
		match = help_fns.findAtUrl(self.hosterRegex, pUrl)

		for m in match:
			gd = m.groupdict()
			if gd['hoster'] in help_fns.knownHosts:
				res.append(ResultBean(gd['hoster'], {"url": self.hosterResultPrefix + gd['url'].replace("&amp;", "&"), 
													 "hoster": gd['hoster'], 
													 "displayName": pDisplayName, 
													 "type": "hoster"}))

		return res
	
	def getLinkByHostUrl(self, url, hoster):
		if hoster in help_fns.knownHosts:
			return help_fns.knownHosts[hoster].getVideoUrl(url)
	
	def handleParameter(self, params):
		url = urllib.unquote(str(params.get("url")))
		urlType = urllib.unquote(str(params.get("type")))
		displayName = urllib.unquote(str(params.get("displayName", "")))
		hosterName = urllib.unquote(str(params.get("hoster", "")))
		folgen = urllib.unquote(str(params.get('folgen', "")))
		addr = urllib.unquote(str(params.get('addr', "")))
		seriesId = urllib.unquote(str(params.get('seriesId', "")))
		season = urllib.unquote(str(params.get('season', '')))
		episode = urllib.unquote(str(params.get('episode', '')))

		if urlType == "film":
			self.showFilm(url, displayName)
		elif urlType == "hoster":
			self.showHoster(url, hosterName, displayName)
		elif urlType == "part":
			self.showPart(url, hosterName, displayName)
		elif urlType == 'staffel':
			self.showStaffel(url, displayName, folgen, addr, seriesId, season)
		elif urlType == 'episode':
			self.showEpisode(url, addr, seriesId, season, episode, displayName)
		else:
			self.searchFilm()

class ResultBean:
	name = ""
	params = {}

	def __init__(self, name, params):
		self.name = name
		self.params = params