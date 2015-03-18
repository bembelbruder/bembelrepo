import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import xbmc  #@UnresolvedImport
import sys
import urllib

import help_fns
from sites.filmpalast import filmpalast

thisPlugin = int(sys.argv[1])

def showVideo(url, hoster, displayName):
	global thisPlugin
	item = xbmcgui.ListItem(url)
	item.setInfo( type="Video", infoLabels={ "Title": displayName })

	print url
	fp = filmpalast.Filmpalast()
	videoUrl = fp.getLinkByHostLink(url, hoster)

	xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(videoUrl, item)
	
def showFilm(url, displayName):
	global thisPlugin

	fp = filmpalast.Filmpalast()
	match = fp.getHostsByFilm(url)

	for m in match:
		addDirectoryItem(m['hoster'], {"urlVideo": m['urlVideo'], "hoster": m['hoster'], "displayName": displayName})
	xbmcplugin.endOfDirectory(thisPlugin)

	
def showContent():
	global thisPlugin
	
	keyboard = xbmc.Keyboard("", "Film suchen")
	keyboard.doModal()

	fp = filmpalast.Filmpalast()
	match = fp.searchFilm(keyboard.getText())
	
	for r in match:
		addDirectoryItem(r['displayName'], {"urlFilm": r['urlFilm'], "displayName": r['displayName']})
	xbmcplugin.endOfDirectory(thisPlugin)

	
def addDirectoryItem(name, parameters={},pic=""):
	li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
	url = sys.argv[0] + '?' + urllib.urlencode(parameters)
	return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
	
params = help_fns.parameters_string_to_dict(sys.argv[2])
urlFilm = str(params.get("urlFilm", ""))
urlVideo = str(params.get("urlVideo", ""))
displayName = str(params.get("displayName", ""))
hosterName = str(params.get("hoster", ""))

if not sys.argv[2]:
	showContent()
else:
	if urlFilm:
		showFilm(urllib.unquote(urlFilm), urllib.unquote(displayName))
	if urlVideo:
		showVideo(urllib.unquote(urlVideo), urllib.unquote(hosterName), urllib.unquote(displayName))
