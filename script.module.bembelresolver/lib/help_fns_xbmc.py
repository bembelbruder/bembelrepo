# coding: utf8

import xbmc #@UnresolvedImport
import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import urllib
import sys
import help_fns

class help_fns_xbmc:
    
    def __init__(self, plugin):
        self.plugin = plugin
    
    def getSearchString(self):
        keyboard = xbmc.Keyboard("", "Film suchen")
        keyboard.doModal()
    
        res = keyboard.getText()
        res = res.replace("ae", "ä")
        res = res.replace("oe", "ö")
        res = res.replace("ue", "ü")
        
        return res
    
    def handleVideoLink(self, url, displayName):
        item = xbmcgui.ListItem(url)
        item.setInfo( type="Video", infoLabels={ "Title": displayName })
    
        xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(url, item)
        
    def handleFileNotExistsException(self):
        xbmc.executebuiltin("Notification(Fehler, Datei nicht gefunden)")
        
    def printResult(self, resultBeanList):
        for m in resultBeanList:
            self.addDirectoryItem(m.name, m.params)
        xbmcplugin.endOfDirectory(self.plugin)
    
    
    def showContent(self, argv, siteObject):
        thisPlugin = int(argv[1])
        params = help_fns.parameters_string_to_dict(argv[2])
    
        siteObject.handleParameter(params, thisPlugin)
    
    def addDirectoryItem(self, name, parameters={},pic=""):
        li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)
