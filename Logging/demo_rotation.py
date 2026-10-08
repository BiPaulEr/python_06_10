import logging, time 
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("roor")
logger.setLevel("DEBUG")

console_handler = TimedRotatingFileHandler("LOL.LOG", when="S", interval=1, backupCount=5)
logger.addHandler(console_handler)

def main():
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL")

for i in range(0, 100000000000000):
    time.sleep(1)
    main()