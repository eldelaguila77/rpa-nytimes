"""Template robot with Python."""
from functions.nytimes import NyTimes
from functions.utils import Utils
from functions.filter_sections import FilterSections
from functions.collecting_data import CollectingData
from functions.export_to_excel import WorkbookExcel
from functions.save_picture_file import SavePictureFile

def minimal_task():
    # The code snippet is performing a series of tasks:
# The code snippet is retrieving the values of the global variables "months", "search_term", and
# "categories" using the function `get_global_variables()`. These global variables are likely used to
# customize the behavior of the robot or provide input data for the tasks it performs.


# The code snippet is checking if the value of the variable `months` is an empty string. If it is,
# it assigns the value 0 to the `months` variable.


# The code snippet `filters(browser, categories)` is calling a function named `filters` and passing
# two arguments: `browser` and `categories`. This function is likely responsible for applying filters
# to the website or web page being accessed by the `browser` object.
    utils = Utils()
    months = utils.get_global_variables("months")
    search_term = utils.get_global_variables("search_term")
    categories = utils.get_global_variables("categories")
    if months == "" :
        months = 0
    nytimes = NyTimes(months, search_term, categories)
    nytimes.open_browser()
    browser = nytimes.open_site()
    filters = FilterSections(browser, categories)
    if len(categories) > 0:
        filters.filters()
    nytimes.show_more()
    collecting_data = CollectingData(browser, search_term)
    news_list_result = collecting_data.get_list_result()
    export_to_excel = WorkbookExcel(news_list_result, search_term)
    export_to_excel.load_constructor()
    export_to_zip = SavePictureFile()
    export_to_zip.export_to_zip()

if __name__ == "__main__":
    minimal_task()
