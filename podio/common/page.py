#General page class
from selenium.webdriver.support.wait import WebDriverWait

class Page(object):
    ELEMENTS = {}

    def __init__(self, driver):
        self.driver = driver

    def __getitem__(self, item):
        if type(self.ELEMENTS[item]) is tuple:
            element = self.find_element(self.ELEMENTS[item][0], self.ELEMENTS[item][1])
        else:
            element = self.driver.find_by_css(self.ELEMENTS[item])[0]
        return element

    def find_element(self, locator, locator_type):
        element = None
        if locator_type == 'css':
            element = self.driver.find_by_css(locator)[0]
        elif locator_type == 'id':
            element = self.driver.find_by_id(locator)
        elif locator_type == 'name':
            element = self.driver.find_by_name(locator)
        return element

    def wait_for_text_present(self, text):
        self.driver.is_text_present(text)
