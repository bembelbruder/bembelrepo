import help_fns

from sites.serien.serie import Serie

class Serien:
    regexSerien = '<li><a href="(?P<url>serie/.*)">(?P<name>.*)</a></li>'

    def getContent(self):
        res = []
        match = help_fns.findAtUrl(self.regexSerien, "http://bs.to/serie-alphabet")
        for m in match:
            x = m.groupdict()
            newSerie = Serie()
            newSerie.name = x['name']
            newSerie.url = x['url']
            res.append(newSerie)
            
        return res
            
