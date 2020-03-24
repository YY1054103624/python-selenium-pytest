from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        self.driver.find_element(*locator).click()