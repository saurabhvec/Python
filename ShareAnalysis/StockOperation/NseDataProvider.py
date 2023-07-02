#imported libraries
import pandas as pd
from pandas_datareader import data as web

class NseDataProvider:
   def __init__(self, scripName, startDate, endDate):
       self.scripName = scripName
       self.startDate = startDate
       self.endDate = endDate

   def getData(self):
       try:
            info = web.DataReader(self.scripName, data_source='yahoo', start=self.startDate, end=self.endDate) 
            return pd.DataFrame(info)
       except:
           msg = ""
       return pd.DataFrame()