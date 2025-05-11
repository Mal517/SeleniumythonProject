import configparser

config = configparser.RawConfigParser
config.read("./Configuration/Login.ini")


class ReadConfig_Login():

    def getUrl(self):
     return config.get(" "," ")
