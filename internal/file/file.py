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

    with open(filename, "r") as f:
        for line in f.readlines():
            site_list.append(line.strip())

    shuffle(site_list)

    return site_list
