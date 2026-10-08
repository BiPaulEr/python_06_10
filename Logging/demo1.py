import logging

logger = logging.getLogger("roor")
logger.setLevel("DEBUG")

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

console_handler2 = logging.StreamHandler()
console_handler2.setLevel("CRITICAL")
logger.addHandler(console_handler2)

def main():
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL")

main()