from abc import ABC, abstractmethod

class CarScraper(ABC):
    #Pure virtual class for scraping car data

    def __init__(self):
        # Common storage for scraped data
        self.carName = []
        self.carKms = []
        self.carPrice = []
        self.carYear = []
        self.carLink = []
        self.url = ''

    @abstractmethod
    def getUrl(self, make=None, year=None):
        #Return the URL for the search query
        pass
    

    @abstractmethod
    def getCars(self, url):
        pass



