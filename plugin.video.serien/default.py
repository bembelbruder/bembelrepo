import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import xbmc #@UnresolvedImport
import xbmcaddon #@UnresolvedImport
import sys
import urllib
import os
import help_fns

from sites.serien.serien import Serien
from sites.serien.serie import Serie
from sites.serien.staffel import Staffel
from sites.serien.folge import Folge
from sites.serien.hoster import Hoster
from hoster.FileNotExistsException import FileNotExistsException

thisPlugin = int(sys.argv[1])
urlHost = "http://www.burning-seri.es/"

def showVideo(hoster):
	global thisPlugin

	try:
		item = xbmcgui.ListItem(hoster.displayName, thumbnailImage = hoster.getImage())
		xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(hoster.getVideoUrl(), item)
	except FileNotExistsException:
		xbmc.executebuiltin("Notification(Fehler, Datei existiert nicht)")

def showContent(siteObject):
	global thisPlugin
	
	for o in siteObject.getContent():
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
siteType = urllib.unquote(str(params.get("type", "")))
hoster = urllib.unquote(str(params.get("hoster", "")))
displayName = urllib.unquote(str(params.get("displayName", "")))

if not sys.argv[2]:
	showContent(Serien())
else:
	if siteType == "serie":
		showContent(Serie(url))
	if siteType == "folge":
		showContent(Folge(url, displayName))
	if siteType == "staffel":
		showContent(Staffel(url))
	if siteType == "hoster":
		showVideo(Hoster(url, hoster, displayName))
