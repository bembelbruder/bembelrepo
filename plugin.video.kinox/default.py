import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import xbmc #@UnresolvedImport
import sys
import urllib

from sites import kinox #@UnresolvedImport
import help_fns #@UnresolvedImport

thisPlugin = int(sys.argv[1])

def showVideo(url, hoster, displayName):
	global thisPlugin
	item = xbmcgui.ListItem(url)
	item.setInfo( type="Video", infoLabels={ "Title": displayName })

	fp = kinox.Kinox()
	parts = fp.getParts(url)
	
	if len(parts) == 0:
		videoUrl = fp.getLinkByHostLink(url, hoster)
		xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(videoUrl, item)
	else:
		showParts(parts, hoster, displayName)
		
def showPart(url, hoster, displayName):
	global thisPlugin
	
	url = "http://kinox.to/aGET/Mirror/" + url
	
	item = xbmcgui.ListItem(url)
	item.setInfo(type="Video", infoLabels={"Title": displayName})
	
	fp = kinox.Kinox()
	videoUrl = fp.getLinkByHostLink(url, hoster)
	xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(videoUrl, item)
		
def showParts(parts, hoster, displayName):
	global thisPlugin
	
	for p in parts:
		addDirectoryItem("Teil " + p[1], {'partVideo': p[0], "hoster": hoster, "displayName": displayName})
	xbmcplugin.endOfDirectory(thisPlugin)
	
def showFilm(url, displayName):
	global thisPlugin

	if isSerie(url):
		showStaffeln(url)
	else:
		fp = kinox.Kinox()
		match = fp.getHostsByFilm(url, True)

		for m in match:
			addDirectoryItem(m['hoster'], {"urlVideo": m['urlVideo'], "hoster": m['hoster'], "displayName": displayName})
		xbmcplugin.endOfDirectory(thisPlugin)

def isSerie(pUrl):
	return len(help_fns.findAtUrl("SeasonSelection", pUrl)) > 0

def showStaffeln(pUrl):
	match = help_fns.findAtUrl('value="([^"]*)" rel="([^"]*)"( selected)?>Staffel \\d{1,2}', pUrl)
	seriesID = help_fns.findAtUrl('SeriesID=[^"]*"', pUrl)
	addr = help_fns.findAtUrl('Addr=[^&]*', pUrl)
	
	for m in match:
		addDirectoryItem("Staffel " + m[0], {"Addr": addr, "Season": m[0], "Episodes": m[1], "SeriesID": seriesID})
	xbmcplugin.endOfDirectory(thisPlugin)

def showStaffel(pAddr, pSeriesID, pSeason, pEpisodes):
	#url = "http://kinox.to/aGET/MirrorByEpisode/?Addr=" + pAddr + "&SeriesID=" + pSeriesID + "&Season=" + pSeason + "&Episode=" + pEpisodes

	for m in pEpisodes:
		addDirectoryItem(m)
	xbmcplugin.endOfDirectory(thisPlugin)

def showContent():
	global thisPlugin
	
	keyboard = xbmc.Keyboard("", "Film suchen")
	keyboard.doModal()
	if (keyboard.isConfirmed()):
		searchtext = keyboard.getText()

	fp = kinox.Kinox()
	match = fp.searchFilm(searchtext)
	
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
partVideo = str(params.get("partVideo", ""))
displayName = str(params.get("displayName", ""))
hosterName = str(params.get("hoster", ""))
seriesID = str(params.get("SeriesID", ""))
season = str(params.get("Season", ""))
episodes = str(params.get("Episodes", ""))
addr = str(params.get("Addr", ""))


if not sys.argv[2]:
	showContent()
else:
	if urlFilm:
		showFilm(urllib.unquote(urlFilm), urllib.unquote(displayName))
	if urlVideo:
		showVideo(urllib.unquote(urlVideo), urllib.unquote(hosterName), urllib.unquote(displayName))
	if seriesID:
		showStaffel(addr, seriesID, season, urllib.unquote(episodes))
	if partVideo:
		showPart(urllib.unquote(partVideo), urllib.unquote(hosterName), urllib.unquote(displayName))
