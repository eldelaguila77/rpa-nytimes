import time
from RPA.Browser.Selenium import Selenium
from SeleniumLibrary.errors import ElementNotFound
from selenium.common.exceptions import StaleElementReferenceException

def show_more(browser: Selenium) -> None:
    """
    The function `show_more` uses a while loop to continuously click a "show more" button on a web page
    until the button is no longer visible or an error occurs.
    
    :param browser: The parameter "browser" is of type Selenium, which is likely a reference to a
    Selenium WebDriver object. This object is used to automate web browser actions, such as navigating
    to URLs, interacting with elements on a webpage, and waiting for certain conditions to be met
    :type browser: Selenium
    """
    #Finals
    btn_show_more = "//button[@data-testid='search-show-more-button']"
    condition = True
    current_url = browser.get_location()
    while condition:
        if browser.get_location() == current_url:
            try:
                browser.wait_until_element_is_visible(btn_show_more, 6)
                browser.set_focus_to_element(btn_show_more)
                browser.click_button(btn_show_more)
            except AssertionError:
                print("Error")
                condition = False
            except ElementNotFound:
                print("btn already not found")
            except StaleElementReferenceException:
                print("stale element reference")
                browser.go_to(current_url)
        else:
            browser.go_to(current_url)