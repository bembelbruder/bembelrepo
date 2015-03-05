import help_fns
import urllib
import re
import cookielib
import urllib2
import HTMLParser
import time

regexPutlocker = 'href="(http://www.putlocker.com/[^"]*)"'
#regexPutlocker ="<iframe src='(.*)' width='\d{0,3}' height='\d{0,3}' frameborder='\d' style='overflow:\W?hidden'></iframe>"
regexPutlocker2 = '<input type="hidden" value="([^"]*)" name="hash">'
regexPlaylist = "playlist: '(.*)'"
regexData = '<title>Video</title><link>(.*)</link><media:content url="(.*\.flv)" type="video/x-flv"'

regexSockshare = 'src="(http://www.sockshare.com/embed/.*)" width'
regexSockshare2 = '<input type="hidden" value="(.*)" name="hash">'
regexDataSockshare = '<title>Video</title>(<link>(.*)</link>)?<media:content url="(.*\.flv)" type="video/x-flv'

regexBitshare = "<a target='_blank' href='(.*)'><img src='asset/img/bsplayer.jpg' alt='Video'></a>"
regexBitshare2 = 'url: "http://bitshare.com/files-ajax/qnhnopys/request.html'
regexBitshareAjaxdl = 'var ajaxdl = "(.*)";'
regexBitshareData = 'url: "(.*)",\n\W*data: "request=generateID&ajaxid="\+ajaxdl,'
regexBitshareAvi = "url: '(.*\.avi)'"

regexStreamcloud = 'http://streamcloud.eu/.*\..{3}\.html'
#regexStreamcloudMP = 'http://streamcloud.eu/.*\.mp4\.html'
regexStreamcloudMP4 = '<input type="hidden" name="op" value="(.*)">\n\W*<input type="hidden" name="usr_login" value="">\n\W*<input type="hidden" name="id" value="(.*)">\n\W*<input type="hidden" name="fname" value="(.*)">\n\W*<input type="hidden" name="referer" value="(.*)">\n\W*<input type="hidden" name="hash" value="">\n\W*<input type="submit" name="imhuman" id="btn_download" class="button gray" value="(.*)">'
regexStreamcloudFile = 'file: "(.*\.mp4)"'

regexMovdivx = 'href="(http://movdivx.com/.*\.flv\.html)"'
regexMovdivx2 = 'type="hidden" name="op" value="(\w*)">\n<input type="hidden" name="usr_login" value="">\n<input type="hidden" name="id" value="(.*)">\n<input type="hidden" name="fname" value="(.*)">'
regexMovdivx3 = "36,42,'(.*)'.split\('\|'\)\)\)" 



def bitshare(url):
	match = help_fns.findAtUrl(regexBitshare, url)
	newUrl = match[0]

	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	link = opener.open(newUrl).read()
	
	print link
	avi = re.compile(regexBitshareAvi).findall(link)
	print avi
	
	ajaxdl = re.compile(regexBitshareAjaxdl).findall(link)[0]
	urldata = re.compile(regexBitshareData).findall(link)[0]
	
	data = {"request": "generateID", "ajaxid": ajaxdl}
	data = urllib.urlencode(data)
	
	link = opener.open(urldata, data).read()
	print link
	
def streamcloud(url):
	[link, newUrl] = help_fns.openUrlGetURL(url)
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	
	link = opener.open(newUrl).read()
	match = re.compile('href="(http://streamcloud[^"]*)"').findall(link)
	print match[0]
	link = opener.open(match[0]).read()
	dataMatch = re.compile(regexStreamcloudMP4).findall(link)
	data = {'op': dataMatch[0][0], 'usr_login': '', 'id': dataMatch[0][1], 'fname': dataMatch[0][2],
			'referer': '', 'hash': '', 'imhuman': dataMatch[0][3]}
	data = urllib.urlencode(data)
	
	time.sleep(11)
	link = opener.open(match[0], data).read()
	match = re.compile(regexStreamcloudFile).findall(link)
	
	return match[0]
	
def sockshare(url):
	newUrl = help_fns.findAtUrl('href="(http://www.sockshare[^"]*)', url)[0]
	
	hash = help_fns.findAtUrl(regexSockshare2, newUrl)[0]
		
	data = {'hash': hash, 'confirm': 'Continue as Free User'}
	data = urllib.urlencode(data)
	
	match = help_fns.findAtUrlWithData(regexPlaylist, newUrl, data)
	
	getFileUrl = "http://www.sockshare.com" + match[0]
	match = help_fns.findAtUrl(regexDataSockshare, getFileUrl)
	
	videoUrl = match[0][2]
	
	return videoUrl.replace("&amp;", "&");	

def putlocker(url):
	newUrl = help_fns.findAtUrl(regexPutlocker, url)[0]

	hash = help_fns.findAtUrl(regexPutlocker2, newUrl)[0]
	
	data = {'hash': hash, 'confirm': "Continue as Free User"}
	data = urllib.urlencode(data)

	match = help_fns.findAtUrlWithData(regexPlaylist, newUrl, data)
	
	getFileUrl = "http://www.putlocker.com" + match[0]
	match = help_fns.findAtUrl(regexDataSockshare, getFileUrl)
	print match

	videoUrl = match[0][2]
	return videoUrl.replace("&amp;", "&");
	
def movdivx(url):
	match = help_fns.findAtUrl(regexMovdivx, url)
	newUrl = match[0]
	
	match = help_fns.findAtUrl(regexMovdivx2, newUrl)
	data = {'op': match[0][0], 'id': match[0][1], 'fname': match[0][2], 'usr_login': '', 'referer': '', 'method_free': 'Continue to Stream'}
	data = urllib.urlencode(data)
	match = help_fns.findAtUrlWithData(regexMovdivx3, newUrl, data)
	
	data = match[0].split("|")
	return data[2] + "://" + data[11] + "." + data[5] + "." + data[4] + ":" + data[27] + "/d/" + data[26] + "/" + data[25] + "." + data[24];