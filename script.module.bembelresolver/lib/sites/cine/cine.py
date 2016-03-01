from sites.BaseSite import BaseSite
import help_fns
import urllib
import json

class Cine(BaseSite):
    
    def __init__(self, dataProvider):
        BaseSite.__init__(self, dataProvider)
        self.searchUrl = "http://www.cine.to/request/search"
        self.searchRegex = '<a href="(?P<url>http://www.filmpalast.to/movies/view/[^"]*)" class="rb">(?P<name>.*)</a>'
        self.hosterRegex = 'class="hostName">(?P<hoster>.*)</p></li>(\\s*.*){4}_blank" href="(?P<url>[^"]*)"'
        self.searchResultPrefix = 'http://cine.to/request/links/'
        
    def getName(self):
        return "Cine"
    
    def getSearchMatch(self):
        #data = (("term", self.dataProvider.getSearchString()), ("count", "8"), ("genre": "0", "kind": "all", "page": "1", "rating": "1"]
        data = (("term", self.dataProvider.getSearchString()), ("count", "8"), ('genre', '0'), ('kind', 'all'), ('page', '1'), ('rating', '1'), ('year[]', '1913'), ('year[]', '2016'))
        data = urllib.urlencode(data)
        print data
        response = json.loads(help_fns.openUrlWithData(self.searchUrl, data))
        
        match = []
        for entry in response['entries']:
            m = {'name': entry['title'], 'url': "#tt" + entry['imdb']}
            match.append(m)
        
        return match
    
    def showHoster(self, url, hosterName, displayName):
        self.showVideoByUrl(url, hosterName, displayName)
