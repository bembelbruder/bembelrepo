import xbmc #@UnresolvedImport
import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import urllib
import sys

import help_fns
from hoster.FileNotExistsException import FileNotExistsException

def showContent(argv, siteObject):
    thisPlugin = int(argv[1])
    params = help_fns.parameters_string_to_dict(argv[2])

    urlFilm = urllib.unquote(str(params.get("urlFilm", "")))
    urlVideo = urllib.unquote(str(params.get("urlVideo", "")))
    displayName = urllib.unquote(str(params.get("displayName", "")))
    hosterName = urllib.unquote(str(params.get("hoster", "")))
    
    if urlFilm:
        showFilm(siteObject, urlFilm, displayName, thisPlugin)
    elif urlVideo:
        showVideo(siteObject, urlVideo, hosterName, displayName, thisPlugin)
    else:
        searchFilm(siteObject, thisPlugin)

def searchFilm(siteObject, plugin):
    keyboard = xbmc.Keyboard("", "Film suchen")
    keyboard.doModal()

    for m in siteObject.searchFilm(keyboard.getText()):
<<<<<<< HEAD
        addDirectoryItem(m.displayName, {"urlFilm": m.url, "displayName": m.displayName})
=======
        print m
        addDirectoryItem(m['displayName'], {"urlFilm": m['urlFilm'], "displayName": m['displayName']})
>>>>>>> branch 'master' of https://github.com/bembelbruder/bembelrepo.git
    xbmcplugin.endOfDirectory(plugin)

def showFilm(siteObject, url, displayName, plugin):
    for m in siteObject.getHostsByFilm(url):
        addDirectoryItem(m['hoster'], {"urlVideo": m['urlVideo'], "hoster": m['hoster'], "displayName": displayName})
    xbmcplugin.endOfDirectory(plugin)

def showVideo(siteObject, url, hoster, displayName, plugin):
    item = xbmcgui.ListItem(url)
    item.setInfo( type="Video", infoLabels={ "Title": displayName })

    try:
        videoUrl = siteObject.getLinkByHostLink(url, hoster)
        xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(videoUrl, item)
    except FileNotExistsException:
        xbmc.executebuiltin("Notification(Fehler, Datei nicht gefunden)")

def addDirectoryItem(name, parameters={},pic=""):
    li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
    url = sys.argv[0] + '?' + urllib.urlencode(parameters)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
