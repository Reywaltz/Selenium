import time
from dataclasses import dataclass
from logging import Logger
from typing import List

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@dataclass
class WebDriver:
    logger: Logger
    driver: webdriver.Chrome

    def login(self, login, password):
        login_field = self.driver.find_element_by_id('index_email')
        password_field = self.driver.find_element_by_id('index_pass')
        login_field.send_keys(login)
        password_field.send_keys(password)

        self.driver.find_element_by_id('index_login_button').click()


    def get_dialog(self):
        self.driver.find_element_by_xpath('//*[@id="l_msg"]/a/span[1]').click()

        self.driver.find_element_by_xpath('//*[@id="im_dialogs"]/div[1]/div[1]/div/div[1]/li[5]')
