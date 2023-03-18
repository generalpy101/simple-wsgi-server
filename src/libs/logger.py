import logging
import os

LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")


def get_logger(name):
    logger = logging.getLogger(name)
    logger.level = logging.__dict__[LOG_LEVEL]
    handler = logging.StreamHandler()

    handler.setFormatter(
        logging.Formatter("%(levelname)s %(asctime)s %(name)s: %(message)s")
    )
    logger.addHandler(handler)
    return logger
