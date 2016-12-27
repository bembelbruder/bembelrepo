# coding: utf8

import xbmc #@UnresolvedImport
import xbmcplugin #@UnresolvedImport
import xbmcgui #@UnresolvedImport
import urllib
import sys
import help_fns
import time

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

class CountdownDialog(object):
    __INTERVALS = 5
    
    def __init__(self, heading, line1='', line2='', line3='', active=True, countdown=60, interval=5):
        self.heading = heading
        self.countdown = countdown
        self.interval = interval
        self.line3 = line3
        if active:
            pd = xbmcgui.DialogProgress()
            if not self.line3: line3 = 'Expires in: %s seconds' % (countdown)
            pd.create(self.heading, line1, line2, line3)
            pd.update(100)
            self.pd = pd
        else:
            self.pd = None

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        if self.pd is not None:
            self.pd.close()
            del self.pd
    
    def start(self, func, args=None, kwargs=None):
        if args is None: args = []
        if kwargs is None: kwargs = {}
        result = func(*args, **kwargs)
        if result:
            return result
        
        start = time.time()
        expires = time_left = self.countdown
        interval = self.interval
        while time_left > 0:
            for _ in range(CountdownDialog.__INTERVALS):
                xbmc.sleep(interval * 1000 / CountdownDialog.__INTERVALS)
                if self.is_canceled(): return
                time_left = expires - int(time.time() - start)
                if time_left < 0: time_left = 0
                progress = time_left * 100 / expires
                line3 = 'Expires in: %s seconds' % (time_left) if not self.line3 else ''
                self.update(progress, line3=line3)
                
            result = func(*args, **kwargs)
            if result:
                return result
    
    def is_canceled(self):
        if self.pd is None:
            return False
        else:
            return self.pd.iscanceled()
        
    def update(self, percent, line1='', line2='', line3=''):
        if self.pd is not None:
            self.pd.update(percent, line1, line2, line3)
