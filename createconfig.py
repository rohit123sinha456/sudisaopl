import configparser
config = configparser.ConfigParser()

config.add_section("ADMIN")
config.set("ADMIN","URL","10.12.1.131")

config.add_section("RABBITMQ")
config.set("RABBITMQ","QUEUE","test")

with open("config.ini",'w') as configfile:
    config.write(configfile)
