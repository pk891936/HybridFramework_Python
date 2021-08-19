import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class readConfig():

    @staticmethod
    def getBrowserPath(browsername):
        browserPath = config.get('driverPathInfo', browsername)
        return browserPath

    @staticmethod
    def getTestDataPath():
        TestDataPath = config.get('testdataInfo', 'testdataPath')
        return TestDataPath

    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('commonInfo', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('commonInfo', 'password')
        return password
