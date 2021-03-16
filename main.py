from selenium import webdriver
from internal.browser import browser
from internal.file import file
from pkg import logger

# TODO
# В текстовом файле содержится список из web – адресов 10 сайтов.
# Считать файл и открыть сайты в случайном порядке.
# Модифицировать список в соответствии с данным порядком
# и закрыть открытые сайты в обратном порядке

log = logger.setup()
sites = file.get_random_sites('sites.txt')
chrome_driver = webdriver.Chrome(executable_path='chromedriver')

driver = browser.WebDriver(log, chrome_driver)


if __name__ == '__main__':
    driver.open_tabs(sites)
    driver.close_tabs_reversed()
