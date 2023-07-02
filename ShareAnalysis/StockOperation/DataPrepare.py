import StockAnalyser.TradeStatusAnalyser as TradeStatusAnalyser

class DataPrepare:
    """This class will prepare data for CSV and EXCEL file"""

    def __init__(self):
        self.__indexValue = []
        self.__priceArray = []
        self.__tda = TradeStatusAnalyser.TradeStatusAnalyser()

    def prepareData(self, inputData):
        """Prepare data from given input data"""
        stockIndex = 0
        for compdata in inputData:
            lengthValue = len(compdata.priceModelList)
            for index in range(lengthValue):
                try:
                    priceMap = []
                    priceMap.insert(0, compdata.scripName)
                    priceMap.insert(1, compdata.companyFullName)
                    priceMap.insert(2, compdata.industryType)
                    priceMap.insert(3, compdata.priceModelList[index].openPrice)
                    priceMap.insert(4, compdata.priceModelList[index].highPrice)
                    priceMap.insert(5, compdata.priceModelList[index].lowPrice)
                    priceMap.insert(6, compdata.priceModelList[index].closePrice)
                    priceMap.insert(7, compdata.priceModelList[index].tradedVolume)
                    priceMap.insert(8, compdata.priceModelList[index].delivarableQuantity)
                    priceMap.insert(9, compdata.priceModelList[index].deliverableQuantityPercent)
                    priceMap.insert(10, compdata.priceModelList[index].tradePLStatement)
                    priceMap.insert(11, self.__tda.analyse(compdata.priceModelList[index].deliverableQuantityPercent))
                    self.__priceArray.insert(stockIndex, priceMap)
                    stockIndex = stockIndex + 1
                    self.__indexValue.append(compdata.priceModelList[index].tradedDate)
                except:
                    print("Error occurrent in DataPrepare # prepareData for Scrip ",compdata.scripName,compdata.priceModelList[index].tradedDate)

    def getPriceArray(self):
        """Return price array value"""
        return self.__priceArray

    def getIndexValue(self):
        """Return Index value"""
        return self.__indexValue


