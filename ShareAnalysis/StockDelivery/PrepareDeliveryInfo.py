import ShareModel.PriceModel as PriceModel
import StockDelivery.StockDeliverySearchOperation as SDSO
import ShareModel.CompanyModel as cm
import datetime

class PrepareDeliveryInfo(object):
    """This class willl prepare delivery information"""
    def __init__(self, singleDate, priceMapArray, originalScripeNameList):
        self.singleDate = singleDate
        self.priceMapArray = priceMapArray
        self.originalScripeNameList = originalScripeNameList
        self.yahooSuffix = ".NS"

    def prepare(self):
        try:
            stockDlvrySrchOprtn = SDSO.StockDeliverySearchOperation(self.singleDate)
            deliveryInfoList = stockDlvrySrchOprtn.execute()
            for delInfo in deliveryInfoList:
                if delInfo.scripName in self.originalScripeNameList:
                    self.updateDeliveryInfo(delInfo)
        except:
            print("Exception occurred in PrepareDeliveryInfo::prepare")

    def updateDeliveryInfo(self, delInfo):
        for priceMap in self.priceMapArray:
            if((priceMap.scripName == delInfo.scripName+self.yahooSuffix)):
                self.updateDeliveryInfoInPriceModelObject(priceMap.priceModelList, delInfo)                

    def updateDeliveryInfoInPriceModelObject(self, priceModelList, delInfo):
        """This will iterate through price model list and update the delivery info"""
        for priceModelObject in priceModelList:
            if(priceModelObject.tradedDate == self.singleDate.strftime('%m/%d/%Y')):
                priceModelObject.delivarableQuantity = delInfo.deliveryQuantity
                priceModelObject.deliverableQuantityPercent = delInfo.deliveryPercent


