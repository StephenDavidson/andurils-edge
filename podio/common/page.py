#General page class
class Page(object):
    ELEMENTS = {}
    FOUND_ELEMENTS = {}

    def __init__(self, driver):
        self.driver = driver

    def __getitem__(self, item):
        if item in self.FOUND_ELEMENTS:
            element = self.FOUND_ELEMENTS[item]
        else:
            if type(self.ELEMENTS[item]) is tuple:
                element = self.find_element(self.ELEMENTS[item][0], self.ELEMENTS[item][1])
            else:
                element = self.driver.find_by_css(self.ELEMENTS[item])[0]
            self.FOUND_ELEMENTS[item] = element
        return element

    def find_element(self, locator, locator_type):
        element = None
        if locator_type == 'css':
            element = self.driver.find_by_css(locator)[0]
        elif locator_type == 'id':
            element = self.driver.find_by_id(locator)
        elif locator_type == 'class':
            element = self.driver.find_by_className(locator)
        elif locator_type == 'name':
            element = self.driver.find_by_name(locator)
        return element