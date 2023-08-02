import os
from RPA.Robocorp.WorkItems import WorkItems
import re

class Utils:

    def __init__(self):
        self

    def get_global_variables(self, global_variable: str) -> str:
        """
        The function `get_global_variables` retrieves a specific global variable from a `WorkItems` object.
        
        :param global_variable: A string representing the name of the global variable you want to retrieve
        :type global_variable: str
        :return: the value of the global variable specified by the input parameter "global_variable".
        """
        #Process
        work_item = WorkItems()
        work_item.get_input_work_item()

        return work_item.get_work_item_variable(global_variable)

    def search_term_count_by_new(self, txt: str, search_term: str) -> int:
        """
        The function `search_term_count_by_new` takes in a string `txt` and a search term `search_term`, and
        returns the count of how many times the search term appears in the text, case-insensitive.
        
        :param txt: The `txt` parameter is a string that represents the text in which you want to search for
        occurrences of a specific term
        :type txt: str
        :param search_term: The `search_term` parameter is a string that represents the term you want to
        search for in the `txt` string
        :type search_term: str
        :return: the total count of the search term in the given text.
        """
        total = txt.lower().count(search_term.lower())
        return total

    def find_money_in_text(self, text: str) -> str:
        """
        The function `find_money_in_text` searches for money values in a given text and returns whether any
        money values were found or not.
        
        :param text: The `text` parameter is a string that represents the text in which you want to find
        money values
        :type text: str
        :return: a string indicating whether or not money is found in the given text. The string will be
        either "True" if money is found or "False" if no money is found.
        """
        pattern = re.compile('|'.join([
            r'\$[\d,]+(\.\d{1,2})?( USD| dollars)?',
            r'\$\d+',
            r'(\b\d+\s+dollars\b)|(\b\d+\s+USD\b)'
        ]))

        result = pattern.search(text)
        found = 'False' if result is None else 'True'

        return found

    def path_to_save_files(self) -> str:
        """
        The function `path_to_save_files` returns the absolute path to the "output" directory, which is
        located two levels above the current file.
        :return: the path to the directory where files should be saved.
        """

        dir_save = "output"

        local_dirname = os.path.dirname

        base_directory = os.path.abspath(local_dirname(local_dirname((__file__))))
        output_path = os.path.join(base_directory, dir_save)

        return output_path 