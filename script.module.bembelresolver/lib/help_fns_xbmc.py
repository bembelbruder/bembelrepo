import xbmc #@UnresolvedImport
import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import urllib
import sys
import help_fns

def getSearchString():
    keyboard = xbmc.Keyboard("", "Film suchen")
    keyboard.doModal()

    return keyboard.getText()

def handleVideoLink(url, displayName):
    item = xbmcgui.ListItem(url)
    item.setInfo( type="Video", infoLabels={ "Title": displayName })

    xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(url, item)
    
def handleFileNotExistsException():
    xbmc.executebuiltin("Notification(Fehler, Datei nicht gefunden)")
    
def printResult(siteObject, plugin):
    for m in siteObject.getListObjects():
        addDirectoryItem(m.name, m.params)
    xbmcplugin.endOfDirectory(plugin)


def showContent(argv, siteObject):
    thisPlugin = int(argv[1])
    params = help_fns.parameters_string_to_dict(argv[2])

    siteObject.handleParameter(params, thisPlugin)

def addDirectoryItem(name, parameters={},pic=""):
    li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
    url = sys.argv[0] + '?' + urllib.urlencode(parameters)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
