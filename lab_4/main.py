import time

import toml
from selenium import webdriver

from internal.browser import browser
from pkg import logger

# TODO
# Открыть Вконтакте.
# Выполнить вход и получить список из 10 последних сообщений.


cfg = toml.load('cfg.toml')

URL = cfg.get('vk').get('URL')
email = cfg.get('vk').get('email')
password = cfg.get('vk').get('password')

log = logger.setup()

chrome_driver = webdriver.Chrome()

wd = browser.WebDriver(log, chrome_driver)


if __name__ == '__main__':
    wd.driver.get(URL)
    wd.login(email, password)
    time.sleep(5)
    wd.get_dialog()
    wd.get_last_messages()
