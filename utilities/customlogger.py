import logging
class logGenerator():
    @staticmethod
    def logGen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        fileHandler = logging.FileHandler('.\\Logs\\automation.log', mode='a')
        #fileHandler = logging.StreamHandler()
        print("Logger file created")
        fileHandler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%d:%m:%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        #logging.basicConfig(filename=".\\Logs\\automation.log",level=logging.INFO, format="%(asctime)s:%(levename)s:%(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")
        #logger= logging.getLogger()
        #logger.setLevel(logging.INFO)
        return logger
