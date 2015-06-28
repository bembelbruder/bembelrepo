from Test.HosterResult import HosterResult
class HosterCollector:
    
    hosterResults = {}
    
    def addHoster(self, hoster, url, result):
        if not self.hosterResults.has_key(hoster):
            self.hosterResults[hoster] = HosterResult()
            
        self.hosterResults[hoster].addUrl(url, result)
        
    
    def getText(self):
        res = ""

        for hoster in self.hosterResults.keys():
            res += hoster
            res += "(" + str(self.hosterResults[hoster].countCorrect()) + ","
            res += str(self.hosterResults[hoster].countNotFound()) + ","
            res += str(self.hosterResults[hoster].countError()) + ","
            res += str(self.hosterResults[hoster].countUnknown()) + ")\n"
            
        return res