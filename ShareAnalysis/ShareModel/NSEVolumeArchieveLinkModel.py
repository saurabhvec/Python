class NSEVolumeArchieveLinkModel(object):
    """This class will create NSE Volume Archieve link"""
    def __init__(self, daz):
        self.tradingDay = daz
        self.extentionValue = ".DAT"
        self.staticLinkValue = "https://www1.nseindia.com/archives/equities/mto/MTO_"
        self.completeLink = self.staticLinkValue + self.tradingDay.strftime('%d') + self.tradingDay.strftime('%m') + str(self.tradingDay.year) + self.extentionValue

    @property
    def tradingDay(self):
        return self._tradingDay

    @tradingDay.setter
    def tradingDay(self, daz):
        self._tradingDay = daz

    @property
    def extentionValue(self):
        return self._extentionValue

    @extentionValue.setter
    def extentionValue(self, extVal):
        self._extentionValue = extVal

    @property
    def staticLinkValue(self):
        return self._staticLinkValue

    @staticLinkValue.setter
    def staticLinkValue(self, sLinkVal):
        self._staticLinkValue = sLinkVal

    @property
    def completeLink(self):
        return self._completeLink

    @completeLink.setter
    def completeLink(self, compLink):
        self._completeLink = compLink


