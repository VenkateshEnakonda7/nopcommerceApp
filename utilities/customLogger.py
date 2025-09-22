import logging
import os


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename= '.\\Logs\\loggerfile.log',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        return logger
