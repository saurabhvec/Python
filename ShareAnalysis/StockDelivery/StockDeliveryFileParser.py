from bs4 import BeautifulSoup
import pandas as pd
import ShareModel.StockDeliveryModel as SDM
import NSEString.StringOperation as SO

class StockDeliveryFileParser(object):
    """This file will parse delivery data"""
    def __init__(self, soup):
        self.soup = soup
        self.stockDeliveryModelList = []

    def parse(self):
        contentSections = self.soup.contents
        count = 0
        customStringOperation = SO.StringOperation()
        for section in contentSections:
            try:
                if count == 0:
                    basicInformationList = section
                else:
                    stockInformation = str(section.string)
                    if(stockInformation.find("Record Type,Sr No,Name of Security") != -1):
                        stockInformationList = customStringOperation.splitNSEStringWithNewLineSeparator(stockInformation)
                        lineCount = 0
                        for deliveryInfo in stockInformationList:
                            if lineCount != 0:
                                self.createDeliveryModel(deliveryInfo, customStringOperation)
                            lineCount = lineCount + 1
                  
            except:
                print("Problem occurrent while parsing delivery file")                          
            count = count+1
        return self.stockDeliveryModelList
            
    def createDeliveryModel(self, deliveryInfoLine, customStringOperation):
        deliveryInfolist = customStringOperation.splitNSEStringWithCommaSeparator(deliveryInfoLine)
        stokDelvryMdl = SDM.StockDeliveryModel()
        stokDelvryMdl.scripName = deliveryInfolist[2]
        stokDelvryMdl.tradedQuantity = deliveryInfolist[4]
        stokDelvryMdl.deliveryQuantity = deliveryInfolist[5]
        stokDelvryMdl.deliveryPercent = deliveryInfolist[6]
        self.stockDeliveryModelList.append(stokDelvryMdl)
