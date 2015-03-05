import re
import urllib
import urllib2
import sys

reqHeader = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'

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
	print tmpText
	rows = []
	for text in tmpText[1:-1]:
		rows.append(begin + text)
	rows.append(begin + tmpText[-1].split(end)[0])
	
	return rows
