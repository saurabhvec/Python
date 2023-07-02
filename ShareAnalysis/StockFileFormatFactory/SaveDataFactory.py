import CSVOperation.CSVDataFormat as CSVDataFormat
import JsonOperation.JsonDataFormat as JsonDataFormat
import ExcelDataOperation.ExcelDataFormat as ExcelDataFormat
class SaveDataFactory:
    """This is factory class. Based on the format it will save the data."""

    def getObject(self, dataFormat):
        if(dataFormat == "csv"):
            return CSVDataFormat.CSVDataFormat()
        elif(dataFormat == "json"):
            return JsonDataFormat.JsonDataFormat()
        elif(dataFormat == "xlsx"):
            return ExcelDataFormat.ExcelDataFormat()
        else:
            return None


