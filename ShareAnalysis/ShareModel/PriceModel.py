class PriceModel(object):
    """This is pojo class. It holds the information about the scrip share price details for each days."""
    

    @property
    def tradedDate(self):
        return self._tradedDate

    @tradedDate.setter
    def tradedDate(self, tradedDate):
        self._tradedDate = tradedDate

    @property
    def highPrice(self):
        return round(self._highPrice, 2)

    @highPrice.setter
    def highPrice(self,highPrice):
        self._highPrice = highPrice

    @property
    def lowPrice(self):
        return round(self._lowPrice, 2)

    @lowPrice.setter
    def lowPrice(self,lowPrice):
        self._lowPrice = lowPrice

    @property
    def tradedVolume(self):
        return round(self._tradedVolume, 2)

    @tradedVolume.setter
    def tradedVolume(self, tradedVolume):
        self._tradedVolume = tradedVolume

    @property
    def openPrice(self):
        return round(self._openPrice, 2)

    @openPrice.setter
    def openPrice(self, openPrice):
        self._openPrice = openPrice

    @property
    def closePrice(self):
        return round(self._closePrice, 2)

    @closePrice.setter
    def closePrice(self, closePrice):
        self._closePrice = closePrice

    @property
    def tradePLStatement(self):
        return round(self._tradePLStatement, 2)

    @tradePLStatement.setter
    def tradePLStatement(self, tradePLStatement):
        self._tradePLStatement = tradePLStatement

    @property
    def delivarableQuantity(self):
        return self._delivarableQuantity

    @delivarableQuantity.setter
    def delivarableQuantity(self, delivarableQuantity):
        self._delivarableQuantity = delivarableQuantity

    @property
    def deliverableQuantityPercent(self):
        return self._deliverableQuantityPercent

    @deliverableQuantityPercent.setter
    def deliverableQuantityPercent(self, deliverableQuantityPercent):
        self._deliverableQuantityPercent = deliverableQuantityPercent
