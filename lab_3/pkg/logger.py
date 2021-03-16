import logging


def setup() -> logging.Logger:
    """Метод инициализации логгера

    :return: Логгер
    :rtype: logging.Logger
    """
    logger = logging.getLogger('test')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(format)

    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger
