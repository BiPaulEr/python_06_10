import logging

logger = logging.getLogger()
logger.setLevel("DEBUG")

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

def init_system_logging():
    logger.debug("<message from DEBUG>")
    logger.info("<message from INFO>")
    logger.warning("<message from WARNING>")
    logger.error("<message from ERROR>")
    logger.critical("<message from CRITICAL>")

init_system_logging()