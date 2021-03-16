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

    def empty_press(self):
        self.driver.find_element_by_class_name('calc-submit').click()
        self.logger.info('Кнопка расчитать нажата')
        time.sleep(2)

        label = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div[10]/div/div')
        if label is not None:
            self.logger.info("Сообщение об ошибке найдена")
            print(label.text)

        return label.text

    def decimal_to_fraction(self):
        select_option_element = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div[1]/select/option[5]').click()
        
        input_field = self.driver.find_element_by_name('dec')
        input_field.send_keys('--0.222')

        self.driver.find_element_by_class_name('calc-submit').click()
        
        error_label = self.driver.find_element_by_id("dec-error")
        if error_label is not None:
            self.logger.info('Ошибка ввода')
            print(error_label.text)

        return error_label.text

    def simple_to_mixed(self):
        select_option_element = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[1]/select/option[3]').click()
        
        input_field_top = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[3]/div[1]/input[1]')
        input_field_top.send_keys(2)

        input_field_bot = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[3]/div[1]/input[2]')
        input_field_bot.send_keys(3)

        self.driver.find_element_by_class_name('calc-submit').click()

        time.sleep(1)
        
        res = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/form/div[3]/div[3]/div")
        if res is not None:
            self.logger.info('Результат выведен')
            print(res.text)

        return res.text

    def percentage_to_fraction(self):
        select_option_element = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[1]/select/option[7]').click()

        input_field = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[7]/input')
        input_field.send_keys(15)

        self.driver.find_element_by_class_name('calc-submit').click()

        time.sleep(1)
        
        res = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/form/div[7]/div[3]")

        if res is not None:
            self.logger.info('Результат выведен')
        return res.text
