import pandas as pd

class CSVFileReader(object):
  def __init__(self, csvFileName, sep):
    self.csvFileName = csvFileName
    self.sep = sep

  def readCSV(self):
    csvData = pd.read_csv(self.csvFileName, delimiter=self.sep)
    return csvData