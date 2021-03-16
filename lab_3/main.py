from internal.browser import browser
from pkg import logger
from selenium import webdriver

# TODO
# В текстовом файле содержится список из web – адресов 10 сайтов.
# Считать файл и открыть сайты в случайном порядке.
# Модифицировать список в соответствии с данным порядком
# и закрыть открытые сайты в обратном порядке

URL = 'https://calcus.ru/kalkulyator-drobej'

log = logger.setup()

chrome_driver = webdriver.Chrome()

wd = browser.WebDriver(log, chrome_driver)


if __name__ == '__main__':
    wd.driver.get(URL)
    wd.decimal_to_fraction()
    # wd.empty_press()