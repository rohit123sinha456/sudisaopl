import logging
import sys

class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

        self.file_handler = logging.FileHandler('out.log')
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(self.formatter)

        self.logger.addHandler(self.file_handler)
        #self.logger.addHandler(JournalHandler())

    def getLog(self):
        return self.logger
