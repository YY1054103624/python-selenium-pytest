from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class homework1:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def find_and_send_key(self, locater, key):
        self.driver.find_element(*locater).send_keys(key)

    def find_and_click(self, locater):
        self.driver.find_element(*locater).click()
        sleep(5)
        self.driver.quit()


# find element by id
use_id = homework1(webdriver.Chrome(), "https://www.baidu.com")
use_id.find_and_send_key((By.ID, "kw"), "松勤")
use_id.find_and_click((By.ID, "su"))

# find element by class_name
use_classname = homework1(webdriver.Chrome(), "https://www.baidu.com")
use_classname.find_and_send_key((By.CLASS_NAME, "s_ipt"), "松勤")
use_classname.find_and_click((By.CLASS_NAME, "s_btn"))

# find element by name
use_name = homework1(webdriver.Chrome(), "https://www.baidu.com")
use_name.find_and_send_key((By.NAME, "wd"), "松勤")
use_name.find_and_click((By.CLASS_NAME, "s_btn"))