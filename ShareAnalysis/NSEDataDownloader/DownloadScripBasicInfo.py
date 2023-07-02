import StockOperation.NseDataProvider as NseDataProvider
import datetime

class DownloadScripBasicInfo(object):
    """This class will download basic information like open price, close price etc."""
    def __init__(self, scripeNameList, startDate, endDate):
        self.scripeNameList = scripeNameList
        self.startDate = startDate
        self.endDate = endDate

    def download(self):
        nseData = NseDataProvider.NseDataProvider(self.scripeNameList, self.startDate.strftime('%m/%d/%Y'), self.endDate.strftime('%m/%d/%Y'))
        return nseData.getData()

