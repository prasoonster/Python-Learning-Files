
# we are using root logger and using logging to print statements

import logging

logging.basicConfig(filename = "file.log", level= logging.INFO, format= "%(asctime)s %(levelname)s %(message)s")
logging.warning("protocal problem : %s : connection reset %d" % ("tcs server",123))
logging.info("i told you so")

logging.getLogger().level                                          # logging.getLogger().level()
