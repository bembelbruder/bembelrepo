import urllib
import help_fns

regexPutlocker = '<a href="(http://www.putlocker.com/file/[^"]*)"' 
regexPutlocker2 = '<input type="hidden" value="(.*)" name="fuck_you">'
regexPlaylist = "playlist: '(.*)'"
regexData = '<title>Video</title><media:content url="(.*\.flv)&amp;domain=putlocker.com" type="video/x-flv"'
regexHash = 'name="hash" value="([^"]*)"'

def getVideoUrl(url):
	match = help_fns.findAtUrl(regexHash, url)

	data = {'hash': match[0], 'imhuman': "Continue as Free User", 'op': 'download1', 'id': id}
	data = urllib.urlencode(data)

	link = help_fns.findAtUrlWithData('file: "([^"]*)"', url, data)
	return link[0]


def getVideoUrl_Outside(url):
	match = help_fns.findAtUrl(regexPutlocker, url)
	
	return getVideoUrl(match[0])
