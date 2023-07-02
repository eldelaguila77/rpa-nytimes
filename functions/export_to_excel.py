import os, logging
from datetime import datetime

from openpyxl import Workbook

from functions.utils import path_to_save_files

# The `WorkbookExcel` class is a Python class that creates an Excel workbook, populates it with data
# from a dataframe, and saves it as a file with a specific name.
class WorkbookExcel:
    
    def __init__(
        self,
        dataframe: list,
        search_term: str
    ):
        self.workbook = Workbook()
        self.worksheet = self.workbook.active
        self.dataframe = dataframe
        self.search_term = search_term

    def columns_name(self) -> None:
        """
        The function `columns_name` appends a list of column headers to a worksheet.
        """
        headers = [
            'title',
            'date',
            'description',
            'image_name',
            'count_search_term',
            'amount_money?'
            ]

        self.worksheet.append(headers)
    
    def set_content(self) -> None:
        """
        The function sets the content of a worksheet in a spreadsheet with data from a dataframe.
        """

        self.worksheet.title = str(self.search_term)

        for row in self.dataframe:
            self.worksheet.append(row)
    
    def save_file(self) -> None:
        """
        The `save_file` function saves a workbook as an Excel file with a dynamically generated
        filename.
        """

        dt_utcnow = datetime.utcnow()
        download_file_name= f"searching_{self.search_term}_results_{dt_utcnow}.xlsx"
        export_path = path_to_save_files()
        save_path = os.path.join(export_path, download_file_name)
        self.workbook.save(save_path)

    def load_constructor(self) -> None:
        """
        The function "load_constructor" performs a series of actions including setting column names,
        setting content, and saving a file.
        """
        self.columns_name()
        self.set_content()
        self.save_file()

def export_to_excel(dataframe: list, search_term: str) -> None:
    """
    The function `export_to_excel` exports a given dataframe to an Excel file.
    
    :param dataframe: The `dataframe` parameter is a list that contains the data that you want to export
    to an Excel file. Each element in the list represents a row in the Excel file
    :type dataframe: list
    :param search_term: The search_term parameter is a string that represents the filename you want to
    save the file
    """
    workbook_excel = WorkbookExcel(dataframe, search_term)
    workbook_excel.load_constructor()