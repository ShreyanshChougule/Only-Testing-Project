import configparser

data = configparser.RawConfigParser()

data.read("C:\\Users\\Tejas\\Only Testing Project\\Configuration\\Config.ini")


class Config_File_Opractions:

    @staticmethod
    def getURL():
        UL = data.get("Main data", "URL")
        return UL
