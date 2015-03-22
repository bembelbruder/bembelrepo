import help_fns

class KKiste:
	def getName(self):
		return "KKiste"

	def searchFilm(self, pSearchString):
		url = "http://kkiste.to/search/?q=" + pSearchString
		
		res = []
		match = help_fns.findAtUrl('<a href="([^"]*)" title="[^"]*" class="title">([^<]*)</a>', url)
		for r in match:
			res.append({"urlFilm": r[0], "displayName": r[1]})

		return res

	def getHostsByFilm(self, pUrl):
		res = []
		match = help_fns.findAtUrl('href="(http://www.ecostream.tv[^"]*)" target="_blank">Ecostream <small>.(.*)\]', "http://kkiste.to" + pUrl)
		
		for m in match:
			res.append({"urlVideo": m[0]})
				
		return res
