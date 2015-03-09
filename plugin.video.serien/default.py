import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import xbmc #@UnresolvedImport
import sys
import urllib

from hoster import streamcloud #@UnresolvedImport
from hoster import sockshare #@UnresolvedImport
from hoster import ecostream #@UnresolvedImport
from hoster import filenuke #@UnresolvedImport
from hoster import videoweed #@UnresolvedImport
from hoster import firedrive #@UnresolvedImport
from hoster import movshare #@UnresolvedImport
from hoster import youwatch #@UnresolvedImport
import help_fns
from hoster import vivo #@UnresolvedImport

regexSerien = '<li><a href="(serie/.*)">(.*)</a></li>'
regexStaffeln = '<li class=" (current)?"><a href="(.*)">(.*)</a></li>'
regexFolgen = '<td>(\d{1,2})</td>\n.*<td><a href="(.*)">\n.*<strong>(.*)</strong>'
regexHoster = 'href="(.*)"><span\n\W*class="icon (.*)"></span> (.*) - Teil 1</a>'
thisPlugin = int(sys.argv[1])
urlHost = "http://www.burning-seri.es/"

knownHosts = {'Streamcloud': streamcloud, 
		'Sockshare': sockshare, 
		'Filenuke': filenuke, 
		'VideoWeed': videoweed,
		'Ecostream': ecostream,
		'Firedrive': firedrive,
		'MovShare': movshare,
		'Vivo': vivo,
		'YouWatch': youwatch}

def showVideo(url, hoster, displayName):
	global thisPlugin

	image = "https:" + help_fns.findAtUrl('<img src="(//s.burning-seri.es/img/cover/[^"]*)" alt="Cover"/>', url)[0]
	print image

	item = xbmcgui.ListItem(displayName, thumbnailImage = image)
	xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(knownHosts[hoster].getVideoUrl_Outside(url), item)

def showFolge(url, displayName):
	global thisPlugin
	
	match = help_fns.findAtUrl(regexHoster, url)
	for m in match:
		if m[2] in knownHosts:
			addDirectoryItem(m[2], {"urlH": m[0], "hoster": m[2], "displayName": displayName})
	xbmcplugin.endOfDirectory(thisPlugin)

def showStaffel(url):
	global thisPlugin
	
	match = help_fns.findAtUrl(regexFolgen, url)
	for m in match:
		addDirectoryItem(m[0] + " - " + m[2], {"urlF": m[1], "displayName": m[2]})
	xbmcplugin.endOfDirectory(thisPlugin)

def showSerie(url):
	global thisPlugin
	
	match = help_fns.findAtUrl(regexStaffeln, url)
	print match
	for m in match:
		addDirectoryItem("Staffel " + m[2], {"urlS": m[1]})
	xbmcplugin.endOfDirectory(thisPlugin)
	
def showContent():
	global thisPlugin
	
	match = help_fns.findAtUrl(regexSerien, urlHost + "serie-alphabet")
	for m in match:
		addDirectoryItem(m[1], {"urlSerie": m[0]})
	xbmcplugin.endOfDirectory(thisPlugin)
	
def addDirectoryItem(name, parameters={},pic=""):
	li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
	url = sys.argv[0] + '?' + urllib.urlencode(parameters)
	return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
	
params = help_fns.parameters_string_to_dict(sys.argv[2])
urlSerie = str(params.get("urlSerie", ""))
urlStaffel = str(params.get("urlS", ""))
urlFolge = str(params.get("urlF", ""))
urlHoster = str(params.get("urlH", ""))
hoster = str(params.get("hoster", ""))
displayName = str(params.get("displayName", ""))

if not sys.argv[2]:
	showContent()
else:
	if urlSerie:
		showSerie(urlHost + urllib.unquote(urlSerie))
	if urlFolge:
		showFolge(urlHost + urllib.unquote(urlFolge), urllib.unquote(displayName))
	if urlStaffel:
		showStaffel(urlHost + urllib.unquote(urlStaffel))
	if urlHoster:
		showVideo(urlHost + urllib.unquote(urlHoster), hoster, urllib.unquote(displayName))
