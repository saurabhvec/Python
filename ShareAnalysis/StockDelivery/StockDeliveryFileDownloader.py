import requests as req
from bs4 import BeautifulSoup
import pandas as pd
import StockDelivery.StockDeliveryFileParser as SDFP

class StockDeliveryFileDownloader(object):
    """This class will download file from the NSE archeive"""
    def __init__(self, nselArchieveLink):
        self.nselArchieveLink = nselArchieveLink

    def download(self):
        soup = self.downloadFromLink()
        fileParser = SDFP.StockDeliveryFileParser(soup)
        return fileParser.parse()

    def downloadFromLink(self):
        page = req.get(self.nselArchieveLink)
        return BeautifulSoup(page.content, 'html.parser')

