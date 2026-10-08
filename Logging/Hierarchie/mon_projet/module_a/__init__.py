import logging 
logger = logging.getLogger(__name__)
logger.propagate = False
handler = logging.FileHandler("OUI.log")
formatter = logging.Formatter(
    "%(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
handler.setLevel(logging.DEBUG)