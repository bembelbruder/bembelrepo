from hoster import vivo
from sites.filmpalast.filmpalast import Filmpalast
from sites.kinox.kinox import Kinox
from sites.kkiste.kkiste import KKiste

#print vivo.Vivo().getVideoUrl("http://vivo.sx/2f06e20a67")

class TestDataProvider:
    def getSearchString(self):
        return "Godzilla"
    
    def printResult(self, res):
        for r in res:
            print r.name + " " + r.params["url"]
            
    def handleVideoLink(self, url, name):
        print "Spiele Video: " + url
        
tdp = TestDataProvider()
fp = Filmpalast(tdp)

#fp.searchFilm()
fp.showHoster("http://streamcloud.eu/22c4iate2xiz/godzilla345ezr6tguhkjl-xvid.avi.html", "Streamcloud.eu", "Godzilla")
#fp.showFilm("http://www.filmpalast.to/movies/view/godzilla-2014", "Godzilla")
#fp.showVideoByUrl('http://www.ecostream.tv/stream/c56825c124058745f3b36cc0212c0e27.html', "Ecostream", "Godzilla")
