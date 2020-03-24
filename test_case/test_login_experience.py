from time import sleep

from selenium import webdriver


class TestDemo:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.10jqka.com.cn/")
        self.driver.implicitly_wait(5)

    def test_login(self):
        self.driver.find_element_by_link_text("登录").click()
        # self.driver.find_element_by_xpath("//*[(@id='username') and (@class='username')]").send_keys("hello world")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.driver.find_element_by_id("username").send_keys("hello world")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("loginBtn").click()

    def teardown(self):
        sleep(3)
        self.driver.quit()