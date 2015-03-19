import help_fns

class Kinox:

	def getName(self):
		return "Kinox"

	def searchFilm(self, pSearchString):
		regex = 'src="/gr/sys/lng/(\\d)\.png" alt="language"></td>\\n\\s*<td.*</td>\\n\\s*<td class="Title"><a href="([^"]*)" onclick="return false;">([^"]*)</a> <span class="Year">(\\d{4})'

		url = "http://kinox.to/Search.html?q=" + pSearchString
		res = []
		match = help_fns.findAtUrl(regex, url)
		for r in match:
			if r[0] == "1":
				res.append({"urlFilm": "http://kinox.to" + r[1], "displayName": r[2] + " - " + r[3]})
		
		return res

	def getHostsByFilm(self, pUrl, pOnlyKnown):
		res = []

		match = help_fns.findAtUrl('rel="([^"]*)">\s<div class="Named">([^>]*)</div>', pUrl)
		for m in match:
			if m[1] in help_fns.knownHosts:
				res.append({"urlVideo": "http://kinox.to/aGET/Mirror/" + m[0], "hoster": m[1]})

		return res
	
	def getLinkByHostLink(self, pUrl, pHoster):
		pUrl = pUrl.replace("&amp;", "&")

		match = help_fns.findAtUrl('<a href=\\\\"[^"]*(http[^"]*)', pUrl)
		res = match[0].replace("\\/", "/")
		res = res.replace("\\", "")
		
		if pHoster in help_fns.knownHosts:
			try:
				return help_fns.knownHosts[pHoster].getVideoUrl(res)
			except:
				return "Fehler bei " + res 
		else:
			return pHoster + " gibt es noch nicht"

	def getParts(self, pUrl):
		pUrl = pUrl.replace("&amp;", "&")
		
		match = help_fns.findAtUrl('<a rel=\\\\"([^"]*)" class=\\\\"[^"]*">Part (\\d)', pUrl)

		return match