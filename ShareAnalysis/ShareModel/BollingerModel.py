class BollingerModel:
    """This is pojo class holds information about bollinger data."""
    @property
    def tradedDate(self):
        return self._tradedDate
    @tradedDate.setter
    def tradedDate(self, tradedDate):
        self._tradedDate = tradedDate
    @property
    def lowerBand(self):
        return round(self._lowerBand, 2)
    @lowerBand.setter
    def lowerBand(self, lowerBand):
        self._lowerBand = lowerBand
    @property
    def upperBand(self):
        return round(self._upperBand, 2)
    @upperBand.setter
    def upperBand(self, upperBand):
        self._upperBand = upperBand
    @property
    def meanValue(self):
        return round(self._meanValue, 2)
    @meanValue.setter
    def meanValue(self, meanValue):
        self._meanValue = meanValue
    @property
    def standardDeviation(self):
        return round(self._standardDeviation, 2)
    @standardDeviation.setter
    def standardDeviation(self, standardDeviation):
        self._standardDeviation = standardDeviation

