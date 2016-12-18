import help_fns

from sites.serienstream.serien import Serien

class Anfangsbuchstaben:
    regexSerien = '<a href="/katalog/(?P<name>[^"]*)"'

    def getContent(self):
        res = []

        match = help_fns.findAtUrl(self.regexSerien, 'http://serienstream.to/serien')        
        for m in match:
            x = m.groupdict()
            newSerie = Serien()
            newSerie.name = x['name']
            newSerie.url = "/katalog/" + x['name']
            res.append(newSerie)
            
        return res
            
