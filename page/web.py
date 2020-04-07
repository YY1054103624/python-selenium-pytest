from selenium import webdriver
from page.main_page import MainPage


class Web:
    def start(self):
        self.driver = webdriver.Chrome(r'D:\software\python36\chromedriver.exe')
        self.driver.get("http://www.10jqka.com.cn/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)
        return MainPage(self.driver)

    def stop(self):
        self.driver.quit()
