import threading
import StockDelivery.PrepareDeliveryInfo as pdi

class StockDeliveryUpdaterThread(threading.Thread):
    """description of class"""
    def __init__(self, scripNameParserObj,  priceMapArray, dateRangeList):
        threading.Thread.__init__(self)
        self.scripNameParserObj = scripNameParserObj
        self.priceMapArray = priceMapArray
        self.dateRangeList = dateRangeList

    def run(self):
        """This will call prepare delivery class to prepare and update delivery information"""
        try:
            for singleDate in self.dateRangeList:
                delivryInfo = pdi.PrepareDeliveryInfo(singleDate,self.priceMapArray,self.scripNameParserObj._originalScripeNameList)
                delivryInfo.prepare()
        except:
            print("Exception occurred in StockDeliveryUpdaterThread")


