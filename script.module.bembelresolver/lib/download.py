import sys
import xbmcgui
import help_fns
import urllib, urlparse
import os
import xbmcaddon

def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("My Script","Downloading File",url)
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()
        
hoster = sys.argv[2]
url = sys.argv[1]
filename = sys.argv[3]

downloadUrl = help_fns.knownHosts[hoster].getVideoUrl_Outside(url)
split = urlparse.urlsplit(downloadUrl)
filename = filename + os.path.splitext(split.path.split("/")[-1])[1]
DownloaderClass(downloadUrl, filename)