# import needed libraries
import datetime
import StockOperation.NseDataProvider as NseDataProvider
import dateutil.relativedelta
import ShareModel.BollingerModel as BollingerModel

class BollingerBand:
    def __init__(self,scripName):
        self.scripName = scripName
        self.__bolingerModelArray = []

    def getInfo(self):
        """This function will work only for single data"""
        startDate = datetime.datetime.today() - datetime.timedelta(days=30)
        endDate = datetime.datetime.today()
        nseData = NseDataProvider.NseDataProvider(self.scripName, startDate.strftime('%m/%d/%Y'), endDate.strftime('%m/%d/%Y'))
        priceData = nseData.getData()
        meanValues = priceData['Close'].rolling(window=20).mean()
        T30DaysStdDeviations = priceData['Close'].rolling(window=20).std()
        upperBands = meanValues + (T30DaysStdDeviations * 2)
        lowerBands = meanValues - (T30DaysStdDeviations * 2)
        self.meanValue = meanValues[endDate.strftime('%Y-%m-%d')]
        self.upperBand = upperBands[endDate.strftime('%Y-%m-%d')]
        self.lowerBand = lowerBands[endDate.strftime('%Y-%m-%d')]
        self.standardDeviation = T30DaysStdDeviations[endDate.strftime('%Y-%m-%d')]

    def getInfo30(self, startDate, endDate):
        """This function is designed to get bollinger information for give date""" 
        self.__bolingerModelArray.clear()       
        delta = datetime.timedelta(days=1)
        while (startDate <= endDate):
            try:
                if (startDate.weekday() < 5):
                    self.__updateBolingerInfo30(startDate)
            except:
                msg = ""
            startDate = startDate + delta
        

    def __updateBolingerInfo30(self, inputDateValue):
        """This function will create bolinger info for 30 days"""
        timeDelta = datetime.timedelta(days=30)
        priceData = self.__getNseData(inputDateValue, timeDelta)     
        if(not priceData.empty):
            meanValues = priceData['Close'].rolling(window=20).mean()
            T30DaysStdDeviations = priceData['Close'].rolling(window=20).std()
            upperBands = meanValues + (T30DaysStdDeviations * 2)
            lowerBands = meanValues - (T30DaysStdDeviations * 2)
            bolinger_model = BollingerModel.BollingerModel()
            bolinger_model.tradedDate = inputDateValue.strftime('%m/%d/%Y')
            bolinger_model.meanValue = meanValues[inputDateValue.strftime('%Y-%m-%d')]
            bolinger_model.upperBand = upperBands[inputDateValue.strftime('%Y-%m-%d')]
            bolinger_model.lowerBand = lowerBands[inputDateValue.strftime('%Y-%m-%d')]
            bolinger_model.standardDeviation = T30DaysStdDeviations[inputDateValue.strftime('%Y-%m-%d')]
            self.__bolingerModelArray.append(bolinger_model)

    def __getNseData(self, startDateValue, timeDelta):
        """This function will evaluate first working days from the start date and then fetch the price data from that date."""        
        start_date = startDateValue - timeDelta
        end_date = startDateValue
        nseData = NseDataProvider.NseDataProvider(self.scripName, start_date.strftime('%m/%d/%Y'), end_date.strftime('%m/%d/%Y'))
        if(nseData.getData().empty):
            self.__getNseData(start_date, timeDelta+1)
        else:
            return nseData.getData()

    def getBolingerDataArray(self):
        return self.__bolingerModelArray
   

