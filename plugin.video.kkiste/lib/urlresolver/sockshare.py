import urllib

from .. import help_fns

regexSockshare2 = '<input type="hidden" value="(.*)" name="hash">'
regexDataSockshare = '<title>Video</title>(<link>(.*)</link>)?<media:content url="(.*\.flv)" type="video/x-flv'

regexPutlocker = 'href="(http://www.sockshare[^"]*)'
#regexPutlocker ="<iframe src='(.*)' width='\d{0,3}' height='\d{0,3}' frameborder='\d' style='overflow:\W?hidden'></iframe>"
regexPutlocker2 = '<input type="hidden" value="(.*)" name="fuck_you">'
regexPlaylist = "playlist: '(.*)'"
regexData = '<title>Video</title><link>(.*)</link><media:content url="(.*\.flv)" type="video/x-flv"'

def getVideoUrl(url):
	hash = help_fns.findAtUrl(regexSockshare2, url)[0]
		
	data = {'hash': hash, 'confirm': 'Continue as Free User'}
	data = urllib.urlencode(data)
	
	match = help_fns.findAtUrlWithData(regexPlaylist, url, data)
	
	getFileUrl = "http://www.sockshare.com" + match[0]
	match = help_fns.findAtUrl(regexDataSockshare, getFileUrl)
	
	videoUrl = match[0][2]
	
	return videoUrl.replace("&amp;", "&");	

def getVideoUrl_Outside(url):
	match = help_fns.findAtUrl(regexPutlocker, url)

	return getVideoUrl(match[0])
