import ShareModel.CompanyModel as CompanyModel
import ShareModel.PriceModel as PriceModel
import datetime

class BasicStockDataCreator(object):
    """This class will create basic stock data"""
    def __init__(self, stockName, stockInfo, startDate, endDate, scripNameParserObj):
        self.stockName = stockName
        self.stockInfo = stockInfo
        self.startDate = startDate
        self.endDate = endDate
        self.scripNameParserObj = scripNameParserObj
        

    def create(self):
        """This function will create basic information."""         
        cm = CompanyModel.Company()
        cm.scripName = self.stockName

        if self.scripNameParserObj._companyFullNameMap[self.stockName]:
            cm.companyFullName = self.scripNameParserObj._companyFullNameMap[self.stockName]

        if self.scripNameParserObj._industryTypeMap[self.stockName]:
            cm.industryType = self.scripNameParserObj._industryTypeMap[self.stockName]

        priceModelList = []
        for singleDate in self.dateRange():
            #This is validate if dataframe have above row or not
            if singleDate in self.stockInfo.index:
                pm = PriceModel.PriceModel()
                pm.tradedDate = singleDate.strftime('%m/%d/%Y')
                pm.openPrice = self.stockInfo.loc[singleDate]['Open', self.stockName]
                pm.highPrice = self.stockInfo.loc[singleDate]['High', self.stockName]
                pm.lowPrice = self.stockInfo.loc[singleDate]['Low', self.stockName]
                pm.closePrice = self.stockInfo.loc[singleDate]['Close', self.stockName]
                pm.tradedVolume = self.stockInfo.loc[singleDate]['Volume', self.stockName]
                pm.tradePLStatement = ((pm.closePrice - pm.openPrice) * 100)/(pm.openPrice)
                priceModelList.append(pm)
        cm.priceModelList = priceModelList
        return cm

    def dateRange(self):
        #This will be used to count range infomation
        for n in range(int ((self.endDate - self.startDate).days)+1):
            yield self.startDate + datetime.timedelta(n)

