from RPA.Browser.Selenium import Selenium
from datetime import datetime, timedelta
from SeleniumLibrary.errors import ElementNotFound
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from functions.logger import logger
from functions.utils import Utils

class NyTimes:

    def __init__(
        self,
        months: str,
        search_term: str,
        categories: str
    ):
        
        self.months = months
        self.search_term = search_term
        self.categories: categories
        self.utils = Utils()

    def open_browser(self) -> None:
        browser = Selenium()
        browser.open_available_browser()
        browser.maximize_browser_window()
        self.browser = browser
        logger.info("browser opened successfully")

    def get_date_range(self):
    # The code block you provided is a function called `get_date_range` that calculates the start and end
    # dates based on the number of months provided.
        number_of_months = int(self.months)
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
        self.start_date_str = start_date_str
        self.end_date_str = end_date_str

    def close_updated_terms(self) -> None :

        #Finals
        terms_button = '//div[@class="css-hqisq1"]//button'

        #Process
        try:
            if self.browser.find_element(terms_button) :
                self.browser.click_element(terms_button)
                logger.info("close update terms was closed")
        except:
            logger.warning("close updated terms was not found")

    
    def click_cookies(self, browser: Selenium) -> None:
        """
        This function accepts cookies on a webpage using RPA Selenium.

        :param browser: An instance of the RPA Browser Selenium class, which is used to automate web browsers
        for testing and web scraping purposes. It allows the script to interact with the web page and perform
        actions such as clicking buttons, filling out forms, and navigating through pages.
        :type browser: RPA.Browser.Selenium.Selenium
        """
        accept_button_xpath = "//button[@data-testid='GDPR-accept']"
        try:
            browser.wait_until_page_contains_element(accept_button_xpath)
            browser.click_element(accept_button_xpath)
            browser.reload_page()
        except Exception as e:
            logger.error("Can't find or interact with cookies button: %s", str(e))

    def show_more(self) -> None:
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
        current_url = self.browser.get_location()
        while condition:
            if self.browser.get_location() == current_url:
                try:
                    self.browser.wait_until_element_is_visible(btn_show_more, 6)
                    self.browser.set_focus_to_element(btn_show_more)
                    self.browser.click_button(btn_show_more)
                except AssertionError:
                    logger.error("Error")
                    condition = False
                except ElementNotFound:
                    logger.warning("btn already not found")
                except StaleElementReferenceException:
                    logger.error("stale element reference")
                    self.browser.go_to(current_url)
                except ElementClickInterceptedException:
                    self.utils.screenshot(self.browser)
                    logger.error("Other element would receive the click")
                    self.browser.wait_until_element_is_visible(btn_show_more, 2)
                    continue
            else:
                self.browser.go_to(current_url)
        

    def open_site(self)  -> Selenium :

        #Process
        # This code is using the RPA.Browser.Selenium library to open a web browser and navigate to a
        # specific URL.
        # The code is calling the `get_date_range` function to obtain the start and end dates based on the
        # number of months provided. It then uses these dates to construct a URL for a search query on the
        # New York Times website. The URL includes the start and end dates as query parameters, along with
        # the search term and sorting option.
        self.get_date_range()
        url = f"https://www.nytimes.com/search?dropmab=false&endDate={self.end_date_str}&query={self.search_term}&sort=best&startDate={self.start_date_str}"
        self.browser.go_to(url)
        self.close_updated_terms()
        self.click_cookies()
        logger.info("site opened successfully")
        return self.browser
    
