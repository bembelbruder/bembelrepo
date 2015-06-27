from sites.BaseSite import BaseSite
from sites.BaseSite import ResultBean
import help_fns

class Kinox(BaseSite):
	
	def __init__(self, dataProvider):
		self.dataProvider = dataProvider
		self.searchUrl = "http://kinox.to/Search.html?q="
		self.searchResultPrefix = "http://kinox.to"
		self.searchRegex = 'src="/gr/sys/lng/(\\d)\.png" alt="language"></td>\\n\\s*<td.*</td>\\n\\s*<td class="Title"><a href="(?P<url>[^"]*)" onclick="return false;">(?P<name>[^"]*)</a> <span class="Year">(\\d{4})'
		self.hosterRegex = 'rel="(?P<url>[^"]*(&amp;Mirror=(?P<mirror>\\d))?)">\s<div class="Named">(?P<hoster>[^>]*)</div> <div class="Data"><b>Mirror</b>: (?P<curHost>\\d{1,2})/(?P<maxHosts>\\d{1,2})<br/>'  
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

	def getHostsByFilm(self, pUrl, pDisplayName):
		res = []
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
