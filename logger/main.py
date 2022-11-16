import logging
import os

import coloredlogs # thu vien them mau sac cho log

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "DEBUG")
LEVEL = {
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
}

logger = logging.getLogger("UX Backend")
# 10 la khoang cach giuaw threadName voi thang truoc no
log_format = "[%(asctime)s|%(threadName)10s|%(levelname)7s|%(filename)10s:%(lineno)03d] %(message)s"
# formatter = logging.Formatter(log_format)

coloredlogs.install(
    logger=logger, milliseconds=True, fmt=log_format, level=LEVEL[LOGGING_LEVEL]
)

print(logger.error("That bai"))
print(logger.warning("Canh bao"))
print(logger.debug("go loi"))
print(logger.info("OK"))
print(LOGGING_LEVEL)


