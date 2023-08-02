from RPA.Browser.Selenium import Selenium
from datetime import datetime, timedelta

def get_date_range(number_of_months: int):
# The code block you provided is a function called `get_date_range` that calculates the start and end
# dates based on the number of months provided.
    number_of_months = int(number_of_months)
    current_date = datetime.now()
    start_current_day = current_date

    if (number_of_months == 1 or number_of_months == 0):
        number_of_months = 0
        current_day = current_date.today().day-1
        current_day
        start_current_day = current_date - timedelta(days=current_day)

    

    start_date = start_current_day - timedelta(days=number_of_months * 30)

    end_date = current_date

    start_date_str = start_date.strftime('%Y%m%d')
    end_date_str = end_date.strftime('%Y%m%d')

    return start_date_str, end_date_str

def open_site(months: int, search: str)  -> Selenium :

    #Process
    # This code is using the RPA.Browser.Selenium library to open a web browser and navigate to a
    # specific URL.
    browser = Selenium()
    # The code is calling the `get_date_range` function to obtain the start and end dates based on the
    # number of months provided. It then uses these dates to construct a URL for a search query on the
    # New York Times website. The URL includes the start and end dates as query parameters, along with
    # the search term and sorting option.
    start_date, end_date = get_date_range(months)
    url = f"https://www.nytimes.com/search?dropmab=false&endDate={end_date}&query={search}&sort=best&startDate={start_date}"
    browser.open_available_browser(url)
    browser.maximize_browser_window()
    return browser

def close_updated_terms(browser: Selenium) -> None :

    #Finals
    terms_button = '//div[@class="css-hqisq1"]//button'

    #Process

    if browser.find_element(terms_button) :
        browser.click_element(terms_button)





