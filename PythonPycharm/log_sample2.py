
# here the purpose is to have separate loggers for employee.py and log_sample.py with separate formats, levels and filenames
# if we don't specify logger, it will take 'root' logger(can check, it prints 'root' in log)

import logging
import employee
import numpy as np

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)                                   # logger.setLevel() - default level

formatter = logging.Formatter('%(asctime)s: %(levelname)s : %(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')                 # logging.FileHandler()
file_handler.setLevel(logging.ERROR)                             # file_handler.setLevel() - means 40, 50 levels will be printed in sample log file
file_handler.setFormatter(formatter)                             # file_handler.setFormatter()

stream_handler = logging.StreamHandler()                         # logging.StreamHandler()
stream_handler.setFormatter(formatter)                           # stream_handler.setFormatter()


logger.addHandler(file_handler)                                  # logger.addHandler()
logger.addHandler(stream_handler)

def fun_divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')              # logger.exception - also shows traceback
    else:
        return result

def fun_log(z):
    """log Function"""
    result = np.log(z)
    logger.error('log of negative no not possible')               # logger.error()
    return result

num_1 = 10
num_2 = 0
num_3 = -4

div_result = fun_divide(num_1, num_2)
log_result = fun_log(num_3)


