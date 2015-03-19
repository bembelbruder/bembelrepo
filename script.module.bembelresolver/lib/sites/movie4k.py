import re
import urllib
import help_fns

from hoster import streamcloud
from hoster import ecostream
from hoster import filenuke
from hoster import movshare

from sites import movie


urlHost = "http://www.movie4k.to/"

regexSearchResult = '<TR id="(coverPreview\d{6,7})">\n\W*<TD width="550" id="tdmovies">\n\W*<a href="(.*)">(.*)<\/a>\n\W*<\/TD>\n\W*\n\W*<TD.*\n(\W*.*\n){0,20}\W*<\/TD>\W*\n\W*<TD.*>\n\W*.*<\/TD>\n\W*<TD.*<\/TD>\n\W*<TD.*src="http:\/\/img\.movie2k\.to\/img\/(.*)".*<\/TD>'
regexPicture = '"\).hover\(function\(e\){\n\W*\$\("body"\)\.append\("<p id=\'coverPreview\'><img src=\'(.*)\' alt=\'Image preview\' width=105 /></p>"\);'
regexFilmHosterList = '<tr id="tablemoviesindex2" >\\r\\n\\s*.*\\r\\n\\s*\\r\\n\\s*<a href="(.*)">(\\d{2}\\.\\d{2}\\.\\d{4}).*\\r\\n\\s*.*\\r\\n\\s*"16" />&#160;(.*)</a>'
regexSerieHosterList = '<a href=\\\\?"(.{0,70}\.html)\\\\?" style=\\\\?"margin-left:18px;\\\\?"><img border=0 style=\\\\?"vertical-align:top;\\\\?" src=\\\\?".*\\\\?" alt=\\\\?".*\\\\?" title=\\\\?".*\\\\?" width=\\\\?"16\\\\?"> &nbsp;(.*)<\/a><\/td><\/tr>'
regexStaffeln = '<OPTION value="(\d{1,2})"( selected)?>Staffel \d{1,2}<\/OPTION>'
regexEpisoden = 'value="([^<>]*)"( selected)?>Episode (\d{1,2})'

regexVideoLink = '<a target="_blank" href="(.*)"><img border=0 src="http://img.movie2k.to/img/click_link.jpg" alt="(.*)" title="(.*)" width="742"></a>'

class Movie4k:
	knownHosts = {'Streamcloud': streamcloud, 
		'Streamclou': streamcloud, 
		'Ecostream': ecostream,
		'Filenuke': filenuke,
		'Movshare': movshare}

	def getName(self):
		return "Movie4k"

	def searchFilm(self, pSearchString):
		url = urlHost + "movies.php?list=search"
		data = {"search": pSearchString}
		data = urllib.urlencode(data)
		
		link = help_fns.openUrlWithData(url, data)
		rows = help_fns.extractText(link, '<TR id="coverPreview', '</TR>')

		res = []
		for r in rows:
			m = movie.Movie(r)
			res.append({"urlFilm": urlHost + m.url, "displayName": m.name, "picture": self.getPicture(m.pictureID, link)})

		return res
		
	def getHostsByFilm(self, pUrl):
		link = help_fns.openUrl(pUrl)
		match = re.compile('&nbsp;(.*)</a></td>.*<a href=\\\\"(.*)\\\\">Quality.*smileys/(\d)').findall(link)
		res = []
		for m in match:
			res.append({"urlVideo": m[1], "hoster": m[0], "quality": m[2]})

		return res

	def getLinkByHostLink(self, pUrl, pHoster):
		if pHoster in self.knownHosts:
			try:
				return self.knownHosts[pHoster].getVideoUrl(pUrl)
			except:
				return "Fehler bei " + pHoster
		else:
			return pHoster + " gibt es noch nicht"

	def getPicture(self, pictureID, link):
		match = re.compile(pictureID + regexPicture).findall(link)
		if match:
			return match[0]
		else:
			return ""
