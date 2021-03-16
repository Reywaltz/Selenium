from internal.browser import browser
from pkg import logger
from selenium import webdriver
import toml

# TODO
#Открыть Вконтакте. 
# Выполнить вход и получить список из 10 последних сообщений.

URL = 'https://vk.com'

cfg = toml.load('cfg.toml')

email = cfg.get('vk').get('email')
password = cfg.get('vk').get('password')

log = logger.setup()

chrome_driver = webdriver.Chrome()

wd = browser.WebDriver(log, chrome_driver)


if __name__ == '__main__':
    wd.driver.get(URL)
    wd.login(email, password)
    # wd.empty_press()