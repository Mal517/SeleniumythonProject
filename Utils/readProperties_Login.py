import configparser

config = configparser.RawConfigParser()
config.read("./Configuration/Login.ini")


class ReadConfig_Login():

    @staticmethod
    def getUrl(self):
        return config.get("Common Details", "url")

    @staticmethod
    def getUsername(self):
        return config.get("Login Details", "username")

    @staticmethod
    def getPassword(self):
        return config.get("Login Details", "password")
