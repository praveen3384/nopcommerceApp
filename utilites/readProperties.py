import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class read_config():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserEmail():
        useremail = config.get('common info', 'username')
        return useremail

    @staticmethod
    def getUserPassword():
        userpassword = config.get('common info', 'password')
        return userpassword


