from RPA.Browser.Selenium import Selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException)
from functions.utils import search_term_count_by_new, find_money_in_text
from functions.save_picture_file import save_picture

import logging

def get_only_image_name(img_url: str) -> str:
    """
    The function `get_only_image_name` takes in an image URL and returns the name of the image without
    any parameters or file extensions.
    
    :param img_url: The `img_url` parameter is a string that represents the URL of an image
    :type img_url: str
    :return: the image name without any parameters or query strings.
    """
    if img_url != 'N/A' :
        char_index_1 = img_url.find('?')
        char_index_2 = img_url.rfind('/')
        image_without_parameters = img_url[char_index_2+1:char_index_1]

        return image_without_parameters
    else:
        return img_url
        

def get_img_from_element(broswer: Selenium, single_new: WebElement) -> str:
    """
    The function `get_img_from_element` takes a Selenium browser object and a WebElement object, and
    returns the source attribute of an image element within the WebElement, or 'N/A' if no image element
    is found.
    
    :param broswer: The parameter "broswer" is expected to be an instance of the Selenium WebDriver
    class, which is used to control the web browser
    :type broswer: Selenium
    :param single_new: The `single_new` parameter is a WebElement object representing a single news
    element on a webpage. It is used to locate the image element within this news element
    :type single_new: WebElement
    :return: a string, which is the source attribute of an image element. If the image element is not
    found, it returns the string 'N/A'.
    """
    img = 'N/A'
    try:
        img_tag = single_new.find_element(By.XPATH, ".//img[@class='css-rq4mmj']")
        img = broswer.get_element_attribute(img_tag, "src")
    except NoSuchElementException:
        logging.error("Can't find element")
    return img


def get_description_from_element(broswer: Selenium, single_new: WebElement) -> str:
    """
    The function `get_description_from_element` retrieves the description text from a web element using
    Selenium and returns it as a string.
    
    :param broswer: The parameter "broswer" is expected to be an instance of the Selenium WebDriver
    class, which is used to interact with a web browser
    :type broswer: Selenium
    :param single_new: The `single_new` parameter is a WebElement object that represents a single news
    element on a webpage. It is used to locate the description tag within this news element
    :type single_new: WebElement
    :return: a string, which is the description extracted from the given web element. If the description
    cannot be found, the function returns 'N/A'.
    """
    description = 'N/A'
    try:
        description_tag = single_new.find_element(By.XPATH, ".//p[@class='css-16nhkrn']")
        description = broswer.get_text(description_tag)
    except NoSuchElementException:
        logging.error("Can't find element")
    return description

def get_list_result(browser: Selenium, search_phrase: str) -> list:
    """
    The function `get_list_result` takes a Selenium browser object and a search phrase as input, and
    returns a list of news articles that match the search phrase, along with additional information such
    as title, date, description, image URL, count of search phrase occurrences, and amount of money
    mentioned in the article.
    
    :param browser: The "browser" parameter is an instance of the Selenium class, which is used to
    interact with a web browser and perform actions like navigating to a webpage, clicking elements, and
    extracting data
    :type browser: Selenium
    :param search_phrase: The search phrase is a string that represents the phrase you want to search
    for in the news list. It could be a keyword or a specific phrase that you want to find in the news
    titles or descriptions
    :type search_phrase: str
    :return: a list of lists. Each inner list contains the following information about a news article:
    """

    #Variables
    news_list = []

    #Finals
    li_news_path = "//li[@data-testid='search-bodega-result']"

    #Process
    news_count = browser.get_element_count(li_news_path)
    news_list_element = browser.get_webelements(li_news_path)

    for new_li in range(news_count):
        li = news_list_element[new_li]
        title_tag = li.find_element(By.XPATH, ".//h4")
        date_tag = li.find_element(By.XPATH, ".//span[@data-testid='todays-date']")
        title = browser.get_text(title_tag)
        date = browser.get_text(date_tag)
        description = get_description_from_element(browser, li)
        img_url = get_img_from_element(browser, li)
        img = get_only_image_name(img_url)
        whole_text = title + ", " + description
        count_search_phrase = search_term_count_by_new(whole_text, search_phrase)
        amount_money = find_money_in_text(whole_text)

        save_picture(img_url, img)

        news_list.append([
                title,
                date,
                description,
                img,
                count_search_phrase,
                amount_money
            ])
    return news_list
