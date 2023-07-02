import ShareModel.NSEVolumeArchieveLinkModel as NSEVAL
import StockDelivery.StockDeliveryFileDownloader as SDFD

class StockDeliverySearchOperation(object):
    """This class will search the delivery % of the stocks"""
    def __init__(self, daz):
        self.daz = daz

    def execute(self):
        nseValModel = NSEVAL.NSEVolumeArchieveLinkModel(self.daz)
        fileDownloader = SDFD.StockDeliveryFileDownloader(nseValModel.completeLink)
        return fileDownloader.download()

