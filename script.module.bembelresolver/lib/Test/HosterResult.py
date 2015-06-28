class HosterResult:
    
    def __init__(self):
        self.__fineUrls = list()
        self.__notFoundUrls = list()
        self.__errorUrls = list()
        self.__unknown = list()
    
    def addUrl(self, url, state):
        if state == 1:
            self.__fineUrls.append(url)
        if state == 2:
            self.__notFoundUrls.append(url)
        if state == 3:
            self.__errorUrls.append(url)
        if state == 4:
            self.__unknown.append(url)
            
    def countCorrect(self):
        return len(self.__fineUrls)
    
    def countNotFound(self):
        return len(self.__notFoundUrls)
    
    def countError(self):
        return len(self.__errorUrls)
    
    def countUnknown(self):
        return len(self.__unknown)