import CSVOperation.CSVFileReader as cfr
import pandas as pd

class ScripeNameReader(cfr.CSVFileReader):
    """This file will read the scripe name list csv file"""

    def __init__(self, scripeNameCsvFile):
        super().__init__(scripeNameCsvFile, ",")
        self._originalScripeNameList = []
        self._yahooFormatNameList = []
        self._companyFullNameMap = {}
        self._industryTypeMap = {}

    @property
    def originalScripeNameList(self):
        return self._originalScripeNameList
    
    @originalScripeNameList.setter
    def originalScripeNameList(self,originalScripeNameList):
        self._originalScripeNameList = originalScripeNameList

    @property
    def yahooFormatNameList(self):
        return self._yahooFormatNameList
    
    @yahooFormatNameList.setter
    def yahooFormatNameList(self,yahooFormatNameList):
        self._yahooFormatNameList = yahooFormatNameList

    def read(self):
        scripNameList = pd.DataFrame(self.readCSV())
        for indices, sn in scripNameList.iterrows(): 
            scripName = str(sn["Symbol"])
            self._originalScripeNameList.append(scripName)
            if(not scripName.endswith(".NS")):
                scripName = scripName + ".NS"
                self._yahooFormatNameList.append(scripName)
                self._industryTypeMap[scripName] = str(sn["Industry"])
                self._companyFullNameMap[scripName] = str(sn["CompanyFullName"])


