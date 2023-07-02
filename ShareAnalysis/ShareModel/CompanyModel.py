import ShareModel.PriceModel as PriceModel
import ShareModel.BollingerModel as BollingerModel

class Company:
    """This is Pojo class holds information about company and share price info"""

    @property
    def scripName(self):
        return self._scripName

    @scripName.setter
    def scripName(self, scripName):
        self._scripName = scripName

    @property
    def priceModelList(self):
        return self._priceModelList

    @priceModelList.setter
    def priceModelList(self, priceModelList):
        self._priceModelList = priceModelList

    @property
    def bolingerModelList(self):
        return self._bolingerModelList

    @bolingerModelList.setter
    def bolingerModelList(self, bolingerModelList):
        self._bolingerModelList = bolingerModelList

    @property
    def industryType(self):
        return self._industryType

    @industryType.setter
    def industryType(self, industryType):
        self._industryType = industryType

    @property
    def companyFullName(self):
        return self._companyFullName

    @companyFullName.setter
    def companyFullName(self, companyFullName):
        self._companyFullName = companyFullName