import threading
import StockDataCreator.BasicStockDataCreator as bsdc

class BasicStockDataCreatorThread(threading.Thread):
    """description of class"""
    def __init__(self, stockNameList, stockInfo, startDate, endDate, scripNameParserObj):
        threading.Thread.__init__(self)
        self.stockNameList = stockNameList
        self.stockInfo = stockInfo
        self.startDate = startDate
        self.endDate = endDate
        self.companyModelList = []
        self.scripNameParserObj = scripNameParserObj

    def run(self):
        try:
            for scripeName in self.stockNameList:
                dataCreator = bsdc.BasicStockDataCreator(scripeName, self.stockInfo, self.startDate, self.endDate, self.scripNameParserObj)
                companyModel = dataCreator.create()
                if companyModel.priceModelList:
                    self.companyModelList.append(companyModel)
        except:
            print("Exception occurred in BasicStockDataCreatorThread")