from time import sleep

from selenium import webdriver

from page.web import Web


class TestDemo:
    def setup(self):
        self.login = Web().start().to_login_page()

    def test_login(self):
        pass

    def teardown(self):
        sleep(3)
        Web().start()