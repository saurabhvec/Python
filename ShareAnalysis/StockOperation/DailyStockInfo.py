# imported libraries
import datetime
import StockOperation.NseDataProvider

class DailyStockInfo:
    def __init__(self, scripName):
        self.scripName = scripName

    def getInfo(self):
        startDate = datetime.datetime.today()
        endDate = datetime.datetime.today()
        #startDate = datetime.datetime.strptime('1/18/2019', '%m/%d/%Y')
        #endDate = datetime.datetime.strptime('1/18/2019', '%m/%d/%Y')
        nseData = NseDataProvider.NseDataProvider(self.scripName, startDate.strftime('%m/%d/%Y'), endDate.strftime('%m/%d/%Y'))
        return nseData.getData()