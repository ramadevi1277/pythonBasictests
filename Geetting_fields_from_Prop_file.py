import configparser

config = configparser.ConfigParser()


config.read("config.properties")


username = config.get("LOGINDETAILS", 'username')
password = config.get("LOGINDETAILS", 'password')


print("Useranme:", username)
print("Password:", password)