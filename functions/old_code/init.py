from RPA.Browser.Selenium import Selenium
import logging
import time
from ..utils import get_date_range

"""
This an old file, the base that I started to make the challenge
"""

def start():
    """
    The function "start" opens the NY Times website using Selenium, maximizes the browser window, and
    then calls the "search" function.
    """

    #Process
    browser = Selenium()
    url = "https://www.nytimes.com/"
    browser.open_available_browser(url)
    browser.maximize_browser_window()
    search(browser)

def search(browser: Selenium):
    """
    The function `search` performs a search on a web browser using Selenium, focusing on the search
    input, entering a phrase to search, and clicking the search button.
    
    :param browser: The parameter "browser" is of type Selenium. It is likely an instance of a Selenium
    WebDriver that is used to automate browser actions
    :type browser: Selenium
    """
    #Variables

    phrase_to_search = "Guatemala"

    #Finals

    search_focus_btn = '//button[@data-test-id="search-button"]'
    search_input_after_focus = '//input[@data-testid="search-input"]'
    search_btn = '//button[@data-test-id="search-submit"]'

    #Process
    time.sleep(12)
    browser.click_button(search_focus_btn)
    browser.input_text_when_element_is_visible(search_input_after_focus, phrase_to_search)
    browser.click_button_when_visible(search_btn)
    filters(browser)

def filters(browser: Selenium):
    """
    The function filters the browser by selecting specific sections and then applying a date filter.
    
    :param browser: The parameter "browser" is of type Selenium. It is likely an instance of the
    Selenium WebDriver class, which is used for automating web browsers. It allows you to interact with
    web elements, perform actions like clicking buttons or filling out forms, and navigate through web
    pages
    :type browser: Selenium
    """
    #Variables

    section_or_types = ["Business", "Books"]

    #Finals
    section_button = '//div[@data-testid="section"]//button'

    #Process
    browser.click_element(section_button)
    for section in section_or_types:
        section_item = f"//label[@class='css-1a8ayg6']//span[contains(text(), '{str(section)}')]"
        browser.click_element(section_item)
    date_filter(browser)


def date_filter(browser: Selenium):
    """
    The function `date_filter` sets a specific date range in a web browser using Selenium.
    
    :param browser: The parameter "browser" is of type Selenium, which suggests that it is an instance
    of the Selenium WebDriver class. This parameter is used to interact with the web browser and perform
    actions such as clicking buttons, inputting text, and pressing keys
    :type browser: Selenium
    """

    #Variables
    selected_month = 3

    #Finals
    button_date_range = '//button[@data-testid="search-date-dropdown-a"]'
    button_specific_dates = "//button[@aria-label='Specific Dates']"
    input_start_date = '//input[@data-testid="DateRange-startDate"]'
    input_end_date = '//input[@data-testid="DateRange-endDate"]'


    #Process
    start_date, end_date = get_date_range(selected_month)
    browser.click_button(button_date_range)
    browser.click_button_when_visible(button_specific_dates)
    browser.input_text_when_element_is_visible(input_start_date, start_date)
    browser.input_text_when_element_is_visible(input_end_date, end_date)
    browser.press_keys(input_end_date, "ENTER")
