import urllib

from .. import help_fns

regexPutlocker = 'href="(http://www.putlocker.com/[^"]*)"'
#regexPutlocker ="<iframe src='(.*)' width='\d{0,3}' height='\d{0,3}' frameborder='\d' style='overflow:\W?hidden'></iframe>"
regexPutlocker2 = '<input type="hidden" value="([^"]*)" name="hash">'
regexPlaylist = "playlist: '(.*)'"
regexData = '<title>Video</title><link>(.*)</link><media:content url="(.*\.flv)" type="video/x-flv"'
regexDataSockshare = '<title>Video</title>(<link>(.*)</link>)?<media:content url="(.*\.flv)" type="video/x-flv'

def getVideoUrl(url):
	hash = help_fns.findAtUrl(regexPutlocker2, url)[0]
	
	data = {'hash': hash, 'confirm': "Continue as Free User"}
	data = urllib.urlencode(data)

	match = help_fns.findAtUrlWithData(regexPlaylist, url, data)
	
	getFileUrl = "http://www.putlocker.com" + match[0]
	match = help_fns.findAtUrl(regexDataSockshare, getFileUrl)
	print match

	videoUrl = match[0][2]
	return videoUrl.replace("&amp;", "&");

def getVideoUrl_Outside(url):
	match = help_fns.findAtUrl(regexPutlocker, url)
	
	return getVideoUrl(match[0])
