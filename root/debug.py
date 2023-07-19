import logging

def debug(message, level=logging.INFO):
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    if level == logging.INFO:
        logging.info(message)
    elif level == logging.WARNING:
        logging.warning(message)
    elif level == logging.ERROR:
        logging.error(message)
    elif level == logging.DEBUG:
        logging.debug(message)
    else:
        logging.critical(message)