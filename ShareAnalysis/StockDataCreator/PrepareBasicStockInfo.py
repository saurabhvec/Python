import StockDataCreator.BasicStockDataCreatorThread as bsdct

class PrepareBasicStockInfo(object):
    """This class will prepare basic informaton"""
    def __init__(self, scripNameParserObj, dateRangeParserObj, downloadedStockInfo):
        self.scripNameParserObj = scripNameParserObj
        self.dateRangeParserObj = dateRangeParserObj
        self.downloadedStockInfo = downloadedStockInfo
        self.preparedStockBasicDataList = []

    def prepare(self):
        basicDataPreparatorThreadList = []

        splitedLists= lambda fullList, splitSize: [fullList[i:i+splitSize] for i in range(0, len(fullList), splitSize)]

        for splitedList in splitedLists(self.scripNameParserObj._yahooFormatNameList, 100):
            #Create multiple thread object
            basicDataThread = bsdct.BasicStockDataCreatorThread(splitedList, self.downloadedStockInfo, self.dateRangeParserObj._startDate, self.dateRangeParserObj._endDate, self.scripNameParserObj)
            basicDataThread.setDaemon(False)
            basicDataThread.start()
            basicDataPreparatorThreadList.append(basicDataThread)

        for basicDataPreparatorThread in basicDataPreparatorThreadList:
            basicDataPreparatorThread.join()

        for basicDataPreparatorThread in basicDataPreparatorThreadList:
            self.preparedStockBasicDataList.append(basicDataPreparatorThread.companyModelList)

        return self.preparedStockBasicDataList