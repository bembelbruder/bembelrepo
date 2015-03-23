import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import xbmc #@UnresolvedImport
import sys
import urllib

import help_fns
from hoster.ecostream import Ecostream

thisPlugin = int(sys.argv[1])

def showVideo(url, hoster, displayName):
	global thisPlugin
	es = Ecostream()
	item = xbmcgui.ListItem(url)
	item.setInfo( type="Video", infoLabels={ "Title": displayName })
	videoUrl = es.getVideoUrl("http:" + urllib.quote(url[5:]))
	
	xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(videoUrl, item)
	
def showFilm(url, displayName):
	global thisPlugin

	match = help_fns.findAtUrl('href="(http://www.ecostream.tv[^"]*)" target="_blank">Ecostream <small>.(.*)\]', "http://kkiste.to" + url)
	
	if len(match) > 1:
		for m in match:
			addDirectoryItem(m[1], {"urlVideo": m[0], "displayName": displayName})
		xbmcplugin.endOfDirectory(thisPlugin)
	else:
		url = "http://kkiste.to" + url
		showVideo(match[0][0], 'Ecostream', displayName)
	

	
def showContent():
	global thisPlugin
	
	keyboard = xbmc.Keyboard("", "Film suchen")
	keyboard.doModal()
	
	url = "http://kkiste.to/search/?q=" + keyboard.getText()
	
	match = help_fns.findAtUrl('<a href="([^"]*)" title="[^"]*" class="title">([^<]*)</a>', url)
	for r in match:
		addDirectoryItem(r[1], {"urlFilm": r[0], "displayName": r[1]})
	xbmcplugin.endOfDirectory(thisPlugin)

	
def addDirectoryItem(name, parameters={},pic=""):
	li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
	url = sys.argv[0] + '?' + urllib.urlencode(parameters)
	return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
	
params = help_fns.parameters_string_to_dict(sys.argv[2])
urlFilm = str(params.get("urlFilm", ""))
urlVideo = str(params.get("urlVideo", ""))
displayName = str(params.get("displayName", ""))

if not sys.argv[2]:
	showContent()
else:
	if urlFilm:
		showFilm(urllib.unquote(urlFilm), urllib.unquote(displayName))
	if urlVideo:
		showVideo(urllib.unquote(urlVideo), "Ecostream", urllib.unquote(displayName))
