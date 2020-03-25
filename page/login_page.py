from selenium.webdriver.common.by import By

from page.base_page import BasePage


class LoginPage(BasePage):
    _username_input_locator = (By.ID, "username")
    _password_input_locator = (By.ID, "password")
    _login_button_locator = (By.ID, "loginBtn")
    _login_success_locator = (By.TAG_NAME, "font")

    def login(self, username, password):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.find_element(self._username_input_locator).send_keys(username)
        self.find_element(self._password_input_locator).send_keys(password)
        self.find_element_and_click(self._login_button_locator)

    def login_success_message(self):
        pass

    def login_fail_message(self):
        return self.find_element(self._login_success_locator).text