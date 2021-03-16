import sys
from random import shuffle
from typing import List


def get_random_sites(filename: str) -> List[str]:
    """Метод получения случайного списка ссылок из файла

    :param filename: Имя файла
    :type filename: str
    :return: Список ссылок в случайном порядке
    :rtype: List[str]
    """
    site_list = []
    try:
        with open(filename, "r") as f:
            for line in f.readlines():
                site_list.append(line.strip())
    except FileNotFoundError:
        sys.exit(f"Error: Исходного файла {filename} не существует")

    if site_list == []:
        sys.exit(f"Error: Исходный файл {filename} пустой")
    shuffle(site_list)

    return site_list
