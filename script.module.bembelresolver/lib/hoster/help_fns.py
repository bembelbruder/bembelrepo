import re
import urllib2

reqHeader = 'Mozilla/5.0 (X11: Ubuntu; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0'

def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

def findAtUrl(regex, url):
    return re.compile(regex).findall(openUrl(url))

def findAtUrlWithData(regex, url, data):
    return re.compile(regex).findall(openUrlWithData(url, data))

def openUrl(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', reqHeader)
    req.add_header('Accept-Language', "de,en-US;q=0.7,en;q=0.3")
    req.add_header('Accept-Encoding', 'None')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close
    return link

def openUrlGetURL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', reqHeader)
    response = urllib2.urlopen(req)
    link = response.read()
    newUrl = response.url
    response.close
    return [link, newUrl]

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
