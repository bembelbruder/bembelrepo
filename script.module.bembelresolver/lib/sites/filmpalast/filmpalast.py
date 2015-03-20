import help_fns

class Filmpalast:

	def getName(self):
		return "Filmpalast"

	def searchFilm(self, pSearchString):
		url = "http://www.filmpalast.to/search/title/" + pSearchString
		res = []
		match = help_fns.findAtUrl('<a href="(http://www.filmpalast.to/movies/view/[^"]*)" class="rb">(.*)</a>', url)
		for r in match:
			res.append({"urlFilm": r[0], "displayName": r[1]})
		
		return res

	def getHostsByFilm(self, pUrl):
		res = []
		match = help_fns.findAtUrl('class="hostName">(.*)</p></li>(\\s*.*){4}_blank" href="([^"]*)"', pUrl)

		for m in match:
			if m[0] in help_fns.knownHosts:
				res.append({"urlVideo": m[2], "hoster": m[0]})

		return res
	
	def getLinkByHostLink(self, pUrl, pHoster):
		if pHoster in help_fns.knownHosts:
			return help_fns.knownHosts[pHoster].getVideoUrl(pUrl)
		else:
			return pHoster + " gibt es noch nicht"

