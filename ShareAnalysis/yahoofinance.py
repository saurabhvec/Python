# imported package
import pandas as pd
import numpy as np
import CSVOperation.CSVFileReader as cfr
import datetime
import string 
import ShareModel.CompanyModel as CompanyModel
import ShareModel.PriceModel as PriceModel
import StockFileFormatFactory.SaveDataFactory as SaveDataFactory
import BollingerOperation.bollinger_details as bollinger_details
import CSVOperation.ScripeNameReader as snr
import CSVOperation.DateRangeReader as drr
import NSEDataDownloader.DownloadScripBasicInfo as dsbi
import StockDataCreator.PrepareBasicStockInfo as pbsi
import StockDelivery.StockDeliveryUpdater as sdu
import logging as NSELogging
import logging.config as NSELoggerConfig


class Yahoofinance:
    """ This is the entry class of stock analysis project """
    def __init__(self, stockListPath, dateRangeFile):
        NSELoggerConfig.fileConfig(".\\NSELogger.ini")
        self.nseLogger = NSELogging.getLogger("NSELogger")
        self.stockListPath = stockListPath
        self.nseLogger.info("Stock List file location is {0}".format(self.stockListPath))
        self.scripNameParserObj = snr.ScripeNameReader(self.stockListPath)
        self.dateRangeFile = dateRangeFile
        self.dateRangeParserObj = drr.DateRangeReader(self.dateRangeFile)
        self.priceMapArray = []
        self.preInit()

    def preInit(self):
        """This can be implement in factory Method using abstrct function in main class"""        
        self.scripNameParserObj.read()        
        self.dateRangeParserObj.read()

    def download(self):
        """This will download all information"""
        self.basicStockInfo = self.downloadBasicScripInfo()
        self.nseLogger.debug("Downloaded Scrip info {0}".format(self.basicStockInfo.to_string()))
        companyModelListArray = self.prepareBasicInfo(self.basicStockInfo)
        self.updatePriceMapArray(companyModelListArray)
        self.updateVolumeDeliveryInfo()
       
    def updatePriceMapArray(self, companyModelListArray):
        for compModlLst in companyModelListArray:
            for compMdl in compModlLst:
                self.priceMapArray.append(compMdl)

    def downloadBasicScripInfo(self):
        """This will call class to download basic information"""
        downloadInfo = dsbi.DownloadScripBasicInfo(self.scripNameParserObj._yahooFormatNameList, self.dateRangeParserObj._startDate, self.dateRangeParserObj._endDate)
        return downloadInfo.download()

    def prepareBasicInfo(self, downloadedStockInfo):
        """This will update Company Model with basic data"""
        basicData = pbsi.PrepareBasicStockInfo(self.scripNameParserObj,self.dateRangeParserObj,downloadedStockInfo)
        return basicData.prepare()

    def updateVolumeDeliveryInfo(self):
        """This function will update volume delivery info"""
        deliveryUpdater = sdu.StockDeliveryUpdater(self.dateRangeParserObj,self.scripNameParserObj,self.priceMapArray)
        deliveryUpdater.update()



# Below is days.csv file format
# StartDay,EndDay
#5/25/2020,6/1/2020

#Below is stockList.csv file format
#Name
#INFY
#PERSISTENT
#
yf = Yahoofinance(".\\stockList.csv", ".\\Days.csv")
yf.download()
###########yf.getStockInformation()
sdf = SaveDataFactory.SaveDataFactory()
#sdoj = sdf.getObject("json")
#if(bool(sdoj)):
   # sdoj.saveData(yf.priceMapArray)
#sdoc = sdf.getObject("csv")
#if(bool(sdoc)):
   #S sdoc.saveData(yf.priceMapArray)
sdoxl = sdf.getObject("xlsx")
if(bool(sdoxl)):
    sdoxl.saveData(yf.priceMapArray)
