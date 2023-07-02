import logging
from RPA.Browser.Selenium import Selenium
import urllib.parse


def get_checkboxes_value(browser: Selenium, btn_type: str) -> list:

    #variables
    checkbox_list = "//input[@data-testid='DropdownLabelCheckbox']"

    #Process
# The code snippet you provided is a function that retrieves the values of checkboxes on a web page
# using Selenium. Here's a breakdown of what each line does:
    browser.click_element(btn_type)
    checkboxes = browser.find_elements(checkbox_list)

    values = []

    for checkbox in checkboxes:
        value = browser.get_element_attribute(checkbox, 'value')
        values.append(value)

    return values



def selected_checkboxes_elements(checkboxes_values: list, categories: list) -> list:
# The code snippet you provided is a function called `selected_checkboxes_elements` that takes in a
# list of checkbox values and a list of categories.
# The line `if section.lower() in value.lower():` is checking if the lowercase version of the
# `section` string is present in the lowercase version of the `value` string.
    encoded_values = []
    categories_not_found = categories.copy()
    for value in checkboxes_values:
        for section in categories:
            if section.lower() in value.lower():
                encoded_values.append(urllib.parse.quote(value))
                categories_not_found.remove(section)
    return encoded_values

def concat_categories_url(encoded_values: list) -> str:
    """
    The function `concat_categories_url` takes a list of encoded values and returns a URL string with
    the values concatenated and URL-encoded.
    
    :param encoded_values: The parameter `encoded_values` is a list of encoded category values
    :type encoded_values: list
    :return: The function `concat_categories_url` returns a string.
    """
    url = ""
    count_items = len(encoded_values)
    for index,item in enumerate(encoded_values):
        if (count_items - 1 == index):
            url = url + item
        else:
            url = url + item + ','
    return urllib.parse.quote(url, safe='%7')


def filters(browser: Selenium, categories: list):
    """
    The function filters the browser based on selected categories by modifying the URL and navigating to
    the new URL.
    
    :param browser: The "browser" parameter is of type Selenium, which is a web automation tool used for
    controlling web browsers through code. It allows you to interact with web elements, navigate through
    web pages, and perform various actions on web pages
    :type browser: Selenium
    :param categories: The `categories` parameter is a list of categories that you want to filter the
    browser by. These categories are used to select checkboxes on the webpage and apply the
    corresponding filters
    :type categories: list
    """
    #Finals
    section_button = '//div[@data-testid="section"]//button'
    type_button = '//div[@data-testid="type"]//button'

    #Process
    
    checkboxes_values_section = get_checkboxes_value(browser, section_button)
    encoded_values_section = selected_checkboxes_elements(checkboxes_values_section, categories)
    new_uri_section = concat_categories_url(encoded_values_section)
    new_uri = browser.get_location()
    if new_uri_section != "":
        new_uri = new_uri + "&sections=" + new_uri_section

    checkboxes_values_type = get_checkboxes_value(browser, type_button)
    encoded_values_type = selected_checkboxes_elements(checkboxes_values_type, categories)
    new_uri_type = concat_categories_url(encoded_values_type)

    if new_uri_type != "":
        new_uri = new_uri + "&types=" + new_uri_type


    if len(encoded_values_section) > 0 or len(encoded_values_type) > 0 :
        browser.go_to(new_uri)
    else:
        logging.error("Categories were not found, finished excecution")
        raise AssertionError
    

    