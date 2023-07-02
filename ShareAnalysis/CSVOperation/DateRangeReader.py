import CSVOperation.CSVFileReader as cfr
import datetime
import pandas as pd

class DateRangeReader(cfr.CSVFileReader):
    """This class will format the date range from the CSV file"""

    def __init__(self, dateRangeCsvFile):
        super().__init__(dateRangeCsvFile, ",")
        self._startDate = ""
        self._endDate = ""

    def read(self):
        dateRangeDfValue = pd.DataFrame(self.readCSV())
        self._startDate = datetime.datetime.strptime(dateRangeDfValue["StartDay"][0], '%m/%d/%Y')
        self._endDate = datetime.datetime.strptime(dateRangeDfValue["EndDay"][0], '%m/%d/%Y')

    @property
    def startDate(self):
        return self._startDate

    @startDate.setter
    def startDate(self, startDate):
        self._startDate = startDate

    @property
    def endDate(self):
        return self._endDate

    @endDate.setter
    def startDate(self, endDate):
        self._endDate = endDate

