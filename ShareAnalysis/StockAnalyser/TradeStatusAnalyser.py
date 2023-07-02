import decimal as dc

class TradeStatusAnalyser:
    """Based on the trading history this class will analyse trade status"""

    def __init__(self):
        self.__defStatus = ['Sell', 'Hold', 'Buy', 'StrongBuy']

    def analyse(self, deliveryQtyPercent):
        """This function will analyse data and return whether to buy or sell stocks"""        
        if dc.Decimal(deliveryQtyPercent) > 70 :
            return self.__defStatus[3]
        elif dc.Decimal(deliveryQtyPercent) < 20 :
            return self.__defStatus[0]
        elif (dc.Decimal(deliveryQtyPercent) > 40) :
            return self.__defStatus[2]
        else:
            return self.__defStatus[1]

