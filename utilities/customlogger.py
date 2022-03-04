import logging,inspect,sys
from logging.handlers import RotatingFileHandler
class logGenerator():
    @staticmethod
    def logGen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        fileHandler = logging.FileHandler('.\\Logs\\automation.log', mode='a')
        #consoleHandler = logging.StreamHandler(sys.stdout)
        print("Logger file created")
        fileHandler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%d:%m:%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        #logger.addHandler(consoleHandler)
        #logging.basicConfig(filename=".\\Logs\\automation.log",level=logging.INFO, format="%(asctime)s:%(levename)s:%(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")
        #logger= logging.getLogger()
        #logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def log_utility(loglevel=logging.DEBUG):
        # Mention logger name
        loggername = inspect.stack()[1][3]
        # Create logger instance
        logger = logging.getLogger(loggername)
        # Set log level (info/warn/error etc)
        logger.setLevel(loglevel)

        # Step2: create console and set level
        lhandler = logging.FileHandler("run.txt","a")
        lhandler.setLevel(loglevel)

        # Step3: define message format
        formatter = logging.Formatter('%(name)s: %(asctime)s: %(levelname)s: %(message)s\n\r',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        # Step4: assign formatter to console
        lhandler.setFormatter(formatter)

        # Step5: assign console to logger
        logger.addHandler(lhandler)
        return logger

    @staticmethod
    def log_utility_1(loglevel=logging.INFO):
        # Mention logger name
        loggername = inspect.stack()[1][3]

        logger = logging.getLogger('')
        logger.setLevel(logging.INFO)
        format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(format)
        logger.addHandler(ch)

        fh = RotatingFileHandler('.\\Logs\\automation.log', mode='a', maxBytes=(1048576 * 5), backupCount=7)
        fh.setFormatter(format)
        logger.addHandler(fh)

        return logger