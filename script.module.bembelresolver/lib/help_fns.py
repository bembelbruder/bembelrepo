import re
import urllib2

from hoster import streamcloud
from hoster import videoweed
from hoster import ecostream
from hoster import firedrive
from hoster import movshare
from hoster import vivo
from hoster import youwatch
from hoster import powerwatch
from hoster import vidstream
from hoster import played
from hoster import nowvideo
from hoster import divxstage

reqHeader = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'

knownHosts = {'Streamcloud': streamcloud.Streamcloud(),
              'Streamcloud.eu': streamcloud.Streamcloud(),
              'StreamCloud.eu': streamcloud.Streamcloud(),
              'Vidstream.in': vidstream.Vidstream(),
              'VidStream.in': vidstream.Vidstream(),
              'Played.to': played.Played(),
              'VideoWeed': videoweed.Videoweed(),
              'Ecostream': ecostream.Ecostream(),
              'Firedrive': firedrive.Firedrive(),
              'MovShare': movshare.Movshare(),
              'Movshare.net': movshare.Movshare(),
              'MovShare.net': movshare.Movshare(),
              'NowVideo.sx': nowvideo.Nowvideo(),
              'DivXStage': divxstage.Divxstage(),
              'Vivo': vivo.Vivo(),
              'Vivo.sx': vivo.Vivo(),
              'YouWatch': youwatch.Youwatch(),
              'Youwatch.org': youwatch.Youwatch(),
              'PowerWatch': powerwatch.Powerwatch()}

def parameters_string_to_dict(parameters):
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

def findAtUrl(regex, url):
    return re.compile(regex).finditer(openUrl(url))

def findAtUrlWithData(regex, url, data):
    return re.compile(regex).findall(openUrlWithData(url, data))

def openUrl(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', reqHeader)
    response = urllib2.urlopen(req)
    link = response.read()
    response.close
    return link

def openUrlWithData(url, data):
    req = urllib2.Request(url)
    req.add_header('User-Agent', reqHeader)
    response = urllib2.urlopen(req, data)
    link = response.read()
    response.close
    return link

def openUrlWithDataAndCookie(url, data, cookie):
    req = urllib2.Request(url)
    req.add_header('User-Agent', reqHeader)
    response = urllib2.urlopen(req, data)
    link = response.read()
    response.close
    return link

def extractText(text, begin, end):
    tmpText = text.split(begin)
    rows = []

    for text in tmpText[1:-1]:
        rows.append(begin + text)
    rows.append(begin + tmpText[-1].split(end)[0])
    
    return rows
