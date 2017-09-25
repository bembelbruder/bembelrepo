from sites.BaseSite import BaseSite
from sites.BaseSite import ResultBean
import help_fns
import re

class Kinox(BaseSite):
	
	def __init__(self, dataProvider):
		self.dataProvider = dataProvider
		self.searchUrl = "http://kinox.to/Search.html?q="
		self.searchResultPrefix = "http://kinox.to"
		self.searchRegex = 'src="/gr/sys/lng/(\\d)\.png" alt="language"></td>\\n\\s*<td.*</td>\\n\\s*<td class="Title"><a href="(?P<url>[^"]*)" onclick="return false;">(?P<name>[^"]*)</a> <span class="Year">(\\d{4})'
		self.hosterRegex = 'rel="(?P<url>[^"]*(&amp;Mirror=(?P<mirror>\\d))?)">\s<div class="Named">(?P<hoster>[^>]*)</div> <div class="Data"><b>Mirror</b>: (?P<curHost>\\d{1,2})/(?P<maxHosts>\\d{1,2})<br />'  
		self.hosterResultPrefix = "http://kinox.to/aGET/Mirror/"
		self.partsRegex = '<a rel=\\\\"([^"]*)" class=\\\\"[^"]*">Part (\\d)'
		
	def getName(self):
		return "Kinox"
	
	def showFilm(self, url, displayName):
		match = help_fns.findAtUrl('id="SeasonSelection" rel="\\?Addr=(?P<addr>[^&]*)&amp;SeriesID=(?P<seriesId>[^"]*)"', url)

		if len(match) == 1:
			x = match[0].groupdict()
			self.showStaffeln(url, displayName, x['addr'], x['seriesId'])
		else:
			BaseSite.showFilm(self, url, displayName)
			
	def showEpisode(self, url, addr, seriesId, season, episode, displayName):
		newUrl = "https://kinox.to/aGET/MirrorByEpisode/?Addr=" + addr + "&SeriesID=" + seriesId + "&Season=" + season + "&Episode=" + episode
		
		print newUrl
		BaseSite.showFilm(self, newUrl, displayName)
	
	def showStaffeln(self, url, displayname, addr, seriesId):
		match = help_fns.findAtUrl('<option value="(?P<url>\\d{1,2})" rel="(?P<folgen>[^"]*)"[^>]*>Staffel \\d{1,2}</option>', url)
		
		res = []
		for m in match:
			x = m.groupdict()
			res.append(ResultBean(x['url'], {'url': url,
											 'displayName': displayname, 
											 'folgen': x['folgen'], 
											 'type': 'staffel',
											 'addr': addr,
											 'seriesId': seriesId,
											 'season': x['url']}))
					
		self.dataProvider.printResult(res)
	
	def isSerie(self, url):
		return help_fns.findAtUrl('SeasonSelection', url)
		
	def showHoster(self, url, hosterName, displayName):
		link = help_fns.openUrl(url)
		parts = self.getParts(link, hosterName, displayName)
		
		if len(parts) < 2:
			self.showVideoByLink(link, hosterName, displayName)
		else:
			self.dataProvider.printResult(parts)

	def showVideoByLink(self, link, hosterName, displayName):
		link = link.replace("\\", "")
		url = re.compile('"Stream":"<a href="([^"]*)"').findall(link)[0]
		url = help_fns.knownHosts[hosterName].getInnerUrlByLink(link)
		self.showVideoByUrl(url, hosterName, displayName)

	def getHostsByFilm(self, pUrl, pDisplayName):
		res = []
		pUrl = pUrl.replace("https", "http")
		print pUrl
		match = help_fns.findAtUrl(self.hosterRegex, pUrl)

		for m in match:
			gd = m.groupdict()
			if gd['hoster'] in help_fns.knownHosts:
				for i in range(1,int(gd['maxHosts']) + 1):
					url =  gd['url'].replace("Mirror=" + gd['curHost'], "Mirror=" + str(i))
					
					res.append(ResultBean(gd['hoster'], {"url": self.hosterResultPrefix + url.replace("&amp;", "&"), 
													 "hoster": gd['hoster'], 
													 "displayName": pDisplayName, 
													 "type": "hoster"}))

		return res
