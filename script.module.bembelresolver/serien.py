import help_fns

regexStaffeln = '<li class=" (current)?"><a href="(.*)">(.*)</a></li>'
regexFolgen = '<td>(\d{1,2})</td>\n.*<td><a href=".*/(.*)">\n.*<strong>(.*)</strong>'
regexHoster = '<li><a\n\W* href=".*/(.*)"><span\n\W*class="icon (.*)"></span> (.*) - Teil 1</a>'

class Serien:
	def getAll(self):
		res = []
		match = help_fns.findAtUrl('<li><a href="serie/(.*)">(.*)</a></li>', 'https://www.burning-seri.es/serie-alphabet')
		for m in match:
			res.append({"Name": m[1], "Url": m[0]})

		return res
	 
	def getStaffs(self, url):
		url = "http://www.burning-seri.es/serie/" + url 
		match = help_fns.findAtUrl(regexStaffeln, url)
		return match

	def getFolgen(self, url):
		url = "http://www.burning-seri.es/serie/" + url
		match = help_fns.findAtUrl(regexFolgen, url)
		return match
	
	def getHoster(self, url):
		url = "http://www.burning-seri.es/serie/" + url
		match = help_fns.findAtUrl(regexHoster, url)
		return match
