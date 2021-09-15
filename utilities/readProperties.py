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
    def getScreenshotPath():
        browserPath = config.get('testdataInfo', 'Screenshot_Path')
        return browserPath

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

    @staticmethod
    def getAPI_URL():
        url = config.get('commonInfo', 'baseAPI_URL')
        return url

    @staticmethod
    def getCoopsAPI_URL():
        url = config.get('commonInfo', 'baseCoopsAPI_URL')
        return url


    @staticmethod
    def getJsonFilePath():
        JsonFilePath = config.get('testdataInfo', 'JsonFilePath')
        return JsonFilePath

    @staticmethod
    def getOutputFilePath():
        JsonFilePath = config.get('testdataInfo', 'OutputPath')
        return JsonFilePath

