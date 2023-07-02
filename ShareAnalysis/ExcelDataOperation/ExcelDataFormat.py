import pandas as pd
import numpy as np
import RowColumnFormatter.ColumnHolder as ColumnHolder
import StockOperation.DataPrepare as DataPrepare
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell

class ExcelDataFormat:
    """This class will prepare excel data formate."""
    __excelFileLocation = "./stockPrice.xlsx"

    def __init__(self):
        self.__dp = DataPrepare.DataPrepare()
        self.__ch = ColumnHolder.ColumnHolder()

    def saveData(self, inputData):
        """ This will save data in xlsx format to specified location. """
        if(bool(inputData)):
            self.__dp.prepareData(inputData)
            pdDataFile = pd.DataFrame(self.__dp.getPriceArray(), self.__dp.getIndexValue(), self.__ch.singleColumnFormat())
            pdDataFile.rename_axis('TradedDate')
            exlWriter = pd.ExcelWriter(self.__excelFileLocation, engine='xlsxwriter', mode='w')
            pdDataFile.to_excel(excel_writer=exlWriter, sheet_name='share', columns=self.__ch.singleColumnFormat(), index=True, index_label=self.__dp.getIndexValue())

            # Get the worksheet
            workbook = exlWriter.book
            worksheet = exlWriter.sheets['share']

            # Freeze first row
            worksheet.freeze_panes(1, 0)

            # Adjusting size of the column
            worksheet.set_column('A:B', 15)
            worksheet.set_column('C:D', 25)
            worksheet.set_column('E:I', 12)
            worksheet.set_column('J:K', 11)
            worksheet.set_column('L:M', 9)

            # Apply conditional format : Highlight Row based on status
            number_rows = len(pdDataFile.index) + 1

            redColrFormat = workbook.add_format({'bg_color': 'orange',
                               'font_color': 'black','bold': True})

            greenColrFormat = workbook.add_format({'bg_color': 'lime',
                               'font_color': 'black','bold': True})

            yellowColrFormat = workbook.add_format({'bg_color': 'yellow',
                               'font_color': 'black','bold': True})

            blueColrFormat = workbook.add_format({'bg_color': 'cyan',
                               'font_color': 'black','bold': True})

            worksheet.conditional_format("$A$2:$M$%d" % (number_rows),
                                                                    {   "type": "formula",
                                                                        "criteria": '=INDIRECT("M"&ROW())="Sell"',
                                                                        "format": redColrFormat
                                                                    })
            worksheet.conditional_format("$A$2:$M$%d" % (number_rows),
                                                                    {   "type": "formula",
                                                                        "criteria": '=INDIRECT("M"&ROW())="Hold"',
                                                                        "format": yellowColrFormat
                                                                    })
            worksheet.conditional_format("$A$2:$M$%d" % (number_rows),
                                                                    {   "type": "formula",
                                                                        "criteria": '=INDIRECT("M"&ROW())="Buy"',
                                                                        "format": greenColrFormat
                                                                    })
            worksheet.conditional_format("$A$2:$M$%d" % (number_rows),
                                                                    {   "type": "formula",
                                                                        "criteria": '=INDIRECT("M"&ROW())="StrongBuy"',
                                                                        "format": blueColrFormat
                                                                    })

            exlWriter.save()


