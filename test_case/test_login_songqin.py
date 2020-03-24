import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver


class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://120.55.190.222:9090/")
        self.driver.implicitly_wait(20)

    @pytest.mark.parametrize("username, passwd, expect", [
        ("testxt", "songqintest", "欢迎登录"),
        ("testxt", "123456", "用户名或密码错误")
    ])
    def test_login(self, username, passwd, expect):
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(passwd)
        self.driver.find_element_by_id("but_login").click()
        if passwd == "songqintest":
            assert expect in self.driver.find_element_by_class_name("form-control").text
        else:
            actual = self.driver.find_element_by_class_name("error").text
            assert expect in actual
            print(actual)

    def teardown(self):
        self.driver.quit()