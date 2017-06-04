import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import xbmc #@UnresolvedImport
import xbmcaddon #@UnresolvedImport
import sys
import urllib
import os
import help_fns

from sites.serienstream.anfangsbuchstaben import Anfangsbuchstaben
from sites.serienstream.serien import Serien
from sites.serienstream.serie import Serie
from sites.serienstream.staffel import Staffel
from sites.serienstream.folge import Folge
from sites.serienstream.hoster import Hoster
from hoster.FileNotExistsException import FileNotExistsException
from copy_reg import pickle

thisPlugin = int(sys.argv[1])
urlHost = "https://serienstream.to/"

def showVideo(hoster):
	global thisPlugin

	try:
		item = xbmcgui.ListItem(hoster.displayName, thumbnailImage = hoster.getImage())
		xbmc.Player().play(hoster.getVideoUrl(), item)
	except FileNotExistsException:
		xbmc.executebuiltin("Notification(Fehler, Datei nicht gefunden)")

def showContent(siteObject):
	global thisPlugin
	
	for o in siteObject.getContent():
		addDirectoryItem(o.name, o.getParams(), o.img, includeDownload=o.isDownloadable())
	xbmcplugin.endOfDirectory(thisPlugin)
	
def addDirectoryItem(name, parameters={},pic="", includeDownload = False):
	li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
	
	if False:
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
url = urllib.unquote(str(params.get("url", "")))
siteType = urllib.unquote(str(params.get("type", "")))
hoster = urllib.unquote(str(params.get("hoster", "")))
displayName = urllib.unquote(str(params.get("displayName", "")))
img = urllib.unquote(str(params.get("img", "")))

if not sys.argv[2]:
	showContent(Anfangsbuchstaben())
else:
	url = urlHost + url

	if siteType == "hoster":
		newObject = Hoster()
		newObject.init(url, hoster, displayName, img)
		showVideo(newObject)
	else:
		if siteType == "serie":
			newObject = Serie()
			newObject.init(url, img)
		elif siteType == "folge":
			newObject = Folge()
			newObject.init(url, displayName, img)
		elif siteType == "staffel":
			newObject = Staffel()
			newObject.init(url, img)
		elif siteType == "serien":
			newObject = Serien()
			newObject.init(url)
		else:
			newObject = Anfangsbuchstaben()
		
		showContent(newObject)