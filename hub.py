from library.configparser import ConfigParser
from controller.controller import HubController

def __main__():
    starting()
    parseConfig()
    pass

def parseConfig():
    con = ConfigParser().parser()
    hub = HubController().startMainLoop(configDict = con)


def starting():
    print("Starting HUB Bessani ASSER")
    print("Scripting from Terminal")
    print("Loading configuration from terminal, so we need read a JSON file")
    print("Checking folder and file - config.json")


if __name__ == "__main__":
    __main__()