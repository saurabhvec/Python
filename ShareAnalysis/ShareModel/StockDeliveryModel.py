class StockDeliveryModel(object):
    """description of class"""

    @property
    def scripName(self):
        return self._scripName

    @scripName.setter
    def scripName(self, scripName):
        self._scripName = scripName

    @property
    def tradedQuantity(self):
        return self._tradedQuantity

    @tradedQuantity.setter
    def tradedQuantity(self, tradedQuantity):
        self._tradedQuantity = tradedQuantity

    @property
    def deliveryQuantity(self):
        return self._deliveryQuantity;

    @deliveryQuantity.setter
    def deliveryQuantity(self, deliveryQuantity):
        self._deliveryQuantity = deliveryQuantity

    @property
    def deliveryPercent(self):
        return self._deliveryPercent

    @deliveryPercent.setter
    def deliveryPercent(self, deliveryPercent):
        self._deliveryPercent = deliveryPercent
