import StockOperation.CompanyObjectHolder as CompanyObjectHolder
import json


class JsonDataFormat:
    """This class will print data into json format"""
    __jsonFileLocation = "./stockPrice.json"
    
    def saveData(self, inputData):
        try:
            """ This will save data in JSON format to specified location. """
            coh = CompanyObjectHolder.CompanyObjectHolder()
            coh.companyAttr = inputData
            companyStocksJson = json.dumps(coh.toJson())
            print("=================================dump===================================================")
            print(companyStocksJson)
            print("===================================end=================================================")
            companyJson = json.loads(companyStocksJson)
            print("=================================load===================================================")
            print(companyJson)
            print("==================================end==================================================")
            with open('./stockPrice.json', 'w') as outfile:
                json.dump(coh.toJson(), outfile)
        except:
            print("Exception occurred in JsonDataFormat.")

