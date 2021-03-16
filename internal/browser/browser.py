import time
from typing import List
from dataclasses import dataclass
from selenium import webdriver
from logging import Logger


@dataclass
class WebDriver:
    logger: Logger
    driver: webdriver.Chrome

    def open_tabs(self, sites: List[str]) -> None:
        """Метод открытия списка вкладок

        :param sites: Список URL адресов
        :type sites: List[str]
        """
        self.driver.get(sites[0])
        self.logger.info(f"Открыта вкладка: {sites[0]}")

        for index, site in enumerate(sites[1::]):
            self.driver.execute_script("window.open();")
            self.driver.switch_to.window(self.driver.window_handles[index+1])
            self.driver.get(site)
            self.logger.info(f"Открыта вкладка: {site}")

    def close_tabs_reversed(self) -> None:
        """Метод закрытия вкладок в обратном порядке"""
        for i in self.driver.window_handles[::-1]:
            self.driver.switch_to.window(i)
            cur_url = self.driver.current_url
            self.driver.close()

            self.logger.info(f'Закрыта вкладка {cur_url}')

            time.sleep(1)

        self.driver.quit()
        self.logger.info('Браузер закрыт')
