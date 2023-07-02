"""Template robot with Python."""
from functions.open_site import open_site
from functions.utils import get_global_variables
from functions.filter_sections import filters
from functions.show_more import show_more
from functions.collecting_data import get_list_result
from functions.export_to_excel import export_to_excel
from functions.save_picture_file import export_to_zip

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
    months = get_global_variables("months")
    search_term = get_global_variables("search_term")
    categories = get_global_variables("categories")
    if months == "" :
        months = 0
    browser = open_site(months, search_term)
    if len(categories) > 0:
        filters(browser, categories)
    show_more(browser)
    news_list_result = get_list_result(browser, search_term)
    export_to_excel(news_list_result, search_term)
    """
    The function `export_to_zip` creates a zip file containing all the files in an images directory.
    """
    export_to_zip()


if __name__ == "__main__":
    minimal_task()
