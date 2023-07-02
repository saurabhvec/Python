import json
import ShareModel.CompanyModel

class CompanyObjectHolder:
    """description of class"""

    @property
    def companyAttr(self):
        return self._companyAttr

    @companyAttr.setter
    def companyAttr(self, companyAttr):
        self._companyAttr = companyAttr    

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

