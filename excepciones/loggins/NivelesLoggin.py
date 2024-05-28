import logging


# NIVELES DE LOGGING:
# INFO = 10
# DEBUG = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Este es un mensaje de tipo INFO")
logging.debug("Este es un mensaje de tipo DEBUG")
logging.warning("Este es un mensaje de tipo WARNING")
logging.error("Este es un mensaje de tipo ERROR")
logging.critical("Este es un mensaje de tipo CRITICAL")


