import time
from dataclasses import dataclass
from logging import Logger

from selenium import webdriver


@dataclass
class WebDriver:
    logger: Logger
    driver: webdriver.Chrome

    def login(self, login: str, password: str):
        """Метод авторизация в ВК

        :param login: Логин пользователя
        :type login: str
        :param password: Пароль пользователя
        :type password: str
        """
        login_field = self.driver.find_element_by_id('index_email')
        password_field = self.driver.find_element_by_id('index_pass')
        login_field.send_keys(login)
        password_field.send_keys(password)

        self.driver.find_element_by_id('index_login_button').click()
        self.logger.info("Успешный вход")

    def get_dialog(self):
        """Метод получения диалогов"""
        self.driver.find_element_by_xpath('//*[@id="l_msg"]/a/span[1]').click()
        self.logger.info("Переход в диалоги успешен")
        time.sleep(2)

    def get_last_messages(self):
        """Метод получения сообщений"""
        messages = self.driver.find_elements_by_class_name("nim-dialog--content")
        self.logger.info("Получены последние 10 сообщений")
        for i in messages[:10]:
            print(i.text.split('\n'), end='\n')
