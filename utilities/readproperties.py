import configparser
config = configparser.RawConfigParser()
config.read("C:\\Users\\hp\\PycharmProjects\\nopommerceApp\\Configutations\\config.ini")

class Readconfig:
    @staticmethod
    def geturl():
        url = config.get('common info','baseurl')
        return url
    @staticmethod
    def getusername():
        email=config.get('common info','username')
        return email
    @staticmethod
    def getpassword():
        password=config.get('common info','password')
        return password
