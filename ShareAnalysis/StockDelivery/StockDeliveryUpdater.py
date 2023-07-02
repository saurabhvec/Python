import StockDelivery.StockDeliveryUpdaterThread as sdut
import datetime

class StockDeliveryUpdater(object):
    """This class will update the Stock Delivery information"""
    def __init__(self, dateRangeParserObj, scripNameParserObj, priceMapArray):
        self.dateRangeParserObj = dateRangeParserObj
        self.scripNameParserObj = scripNameParserObj
        self.priceMapArray = priceMapArray

    def update(self):
        """This will call thread to update the delivery information"""
        listOfDeliveryUpdaterThread = []
        splitedDateRangeLists =  lambda fullList, splitSize: [fullList[i:i+splitSize] for i in range(0, len(fullList), splitSize)]

        testDateL = splitedDateRangeLists(self.dateRange(self.dateRangeParserObj._startDate,self.dateRangeParserObj._endDate), 5)

        for splitedDateRangeList in splitedDateRangeLists(self.dateRange(self.dateRangeParserObj._startDate,self.dateRangeParserObj._endDate), 5):
            updaterThread = sdut.StockDeliveryUpdaterThread(self.scripNameParserObj, self.priceMapArray, splitedDateRangeList)
            updaterThread.setDaemon(False)
            updaterThread.start()
            listOfDeliveryUpdaterThread.append(updaterThread)

        for stockDelUpdaterTh in listOfDeliveryUpdaterThread:
            stockDelUpdaterTh.join()

    def dateRange(self, startDate, endDate):
        test11 = [startDate + datetime.timedelta(days=x) for x in range(0, ((endDate - startDate).days + 1))]
        return [startDate + datetime.timedelta(days=x) for x in range(0, ((endDate - startDate).days + 1))]
