import help_fns

from sites.serien.serie import Serie

urlHost = "http://www.burning-seri.es/"

class Serien:
    regexSerien = '<li><a href="(serie/.*)">(.*)</a></li>'

    def getContent(self):
        res = []
        match = help_fns.findAtUrl(self.regexSerien, urlHost + "serie-alphabet")
        for m in match:
            newSerie = Serie()
            newSerie.name = m[1]
            newSerie.url = m[0]
            res.append(newSerie)
            
        return res
            
