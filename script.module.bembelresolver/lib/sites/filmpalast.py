import help_fns #@UnresolvedImport
from hoster import streamcloud #@UnresolvedImport
from hoster import movshare #@UnresolvedImport
from hoster import youwatch #@UnresolvedImport
from hoster import vidstream #@UnresolvedImport
from hoster import played #@UnresolvedImport

class Filmpalast:
	knownHosts = {'Streamcloud.eu': streamcloud,
		'Movshare.net': movshare,
		'Youwatch.org': youwatch,
		'Vidstream.in': vidstream,
		'Played.to': played}


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
			if m[0] in self.knownHosts:
				res.append({"urlVideo": m[2], "hoster": m[0]})

		return res
	
	def getLinkByHostLink(self, pUrl, pHoster):
		if pHoster in self.knownHosts:
			try:
				return self.knownHosts[pHoster].getVideoUrl(pUrl)
			except:
				return "Fehler bei " + pUrl
		else:
			return pHoster + " gibt es noch nicht"


