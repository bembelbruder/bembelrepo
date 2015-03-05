import help_fns
import re
import urllib

def getVideoUrl(url):
	link = help_fns.openUrl(url)

	cid = re.compile('cid="([^"]*)"').findall(link)[0]
	key = re.compile('key="([^"]*)"').findall(link)[0]

	data = {"cid": cid, "file": file, "key": key}
	data = urllib.urlencode(data)

	match = help_fns.findAtUrl("url=([^&]*)", "http://www.movshare.net/api/player.api.php?" + data)

	return match[0]

def getVideoUrl_Outside(url):
	match = help_fns.findAtUrl('href="(http://www.movshare.net/[^"]*)"', url)
	print match
	return getVideoUrl(match[0])
