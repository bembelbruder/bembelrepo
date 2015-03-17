import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import xbmc #@UnresolvedImport
import xbmcaddon #@UnresolvedImport
import sys
import urllib
import os
from sites import serien
from lib import help_fns #@UnresolvedImport

thisPlugin = int(sys.argv[1])
urlHost = "http://www.burning-seri.es/"

def showVideo(hoster):
	global thisPlugin

	item = xbmcgui.ListItem(hoster.displayName, thumbnailImage = hoster.getImage())
	xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(hoster.getVideoUrl(), item)

def showContent(object):
	global thisPlugin
	
	for o in o.getContent():
		addDirectoryItem(o.name, o.getParams, includeDownload=o.isDownloadable())
	xbmcplugin.endOfDirectory(thisPlugin)
	
def addDirectoryItem(name, parameters={},pic="", includeDownload = False):
	li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
	
	if includeDownload:
		scriptPath = getCurrentPath() + "/../script.module.bembelresolver/lib/download.py"
		videoDir = xbmcaddon.Addon(id="plugin.video.serien").getSetting("downloadDir")

		commands = []
		commands.append(("runterladen", "XBMC.RunScript(" + scriptPath + "," +
						" http://www.burning-seri.es/" + parameters['url'] + ", " + 
						parameters['hoster'] + ", " +
						videoDir + parameters['displayName'] + ")"))
		li.addContextMenuItems(commands, True)
		
	url = sys.argv[0] + '?' + urllib.urlencode(parameters)
	return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
	
def getCurrentPath():
    return os.path.dirname(os.path.realpath(__file__))
   
params = help_fns.parameters_string_to_dict(sys.argv[2])
url = urlHost + urllib.unquote(str(params.get("url", "")))
type = urllib.unquote(str(params.get("type", "")))
hoster = urllib.unquote(str(params.get("hoster", "")))
displayName = urllib.unquote(str(params.get("displayName", "")))

if not sys.argv[2]:
	showContent(serie.Serien())
else:
	if type == "serie":
		showContent(serie.Serie(url))
	if type == "folge":
		showContent(serie.Folge(url, displayName))
	if type == "staffel":
		showContent(serie.Staffel(url))
	if urlHoster:
		showVideo(serie.Hoster(url, hoster, displayName))
