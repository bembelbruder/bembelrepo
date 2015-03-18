import urllib
import help_fns

regexPutlocker = '<a href="(http://www.putlocker.com/file/[^"]*)"' 
regexPutlocker2 = '<input type="hidden" value="(.*)" name="fuck_you">'
regexPlaylist = "playlist: '(.*)'"
regexData = '<title>Video</title><media:content url="([^"]*)"'
regexHash = 'value="([^"]*)" name="hash"'

def getVideoUrl(url):
	print url
	match = help_fns.findAtUrl(regexHash, url)

	data = {'hash': match[0], 'confirm': "Continue as Free User"}
	data = urllib.urlencode(data)

	link = help_fns.openUrlWithData(url, data)
	print link
	match = help_fns.findAtUrlWithData(regexPlaylist, url, data)
	getFileUrl = "http://www.putlocker.com" + match[0]
	print help_fns.openUrl(getFileUrl)
	videoUrl = help_fns.findAtUrl(regexData, getFileUrl)[0]

	return videoUrl.replace("&amp;", "&");

def getVideoUrl_Outside(url):
	match = help_fns.findAtUrl(regexPutlocker, url)
	
	return getVideoUrl(match[0])

def getDownloadCommand():
	return ""