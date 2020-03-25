from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.login_page import LoginPage


class MainPage(BasePage):
    login_page_locator = (By.LINK_TEXT, "登录")

    def to_login_page(self):
        self.find_element_and_click(self.login_page_locator)
        return LoginPage(self.driver)