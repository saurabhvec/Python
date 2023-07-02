import pandas as pd
import ShareModel.CompanyModel as CompanyModel
import ShareModel.BollingerModel as BollingerModel
import ShareModel.PriceModel as PriceModel
import StockOperation.DataPrepare as DataPrepare
import RowColumnFormatter.ColumnHolder as ColumnHolder

class CSVDataFormat:
    """This class will save data in CSV format"""
    __csvFileLocation = "./stockPrice.csv"

    def __init__(self):
        self.__dp = DataPrepare.DataPrepare()
        self.__ch = ColumnHolder.ColumnHolder()

    def saveData(self, inputData):
        """ This will save data in CSV format to specified location. """
        if(bool(inputData)):
            try:
                self.__dp.prepareData(inputData)
                pdDataFile = pd.DataFrame(self.__dp.getPriceArray(), self.__dp.getIndexValue(), self.__ch.singleColumnFormat())
                pdDataFile.to_csv(self.__csvFileLocation)
            except:
                print("Error Occurred while saving CSVDataFormat::saveData")
