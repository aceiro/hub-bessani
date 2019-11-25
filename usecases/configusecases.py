from entities.meliapientity import MeLiApi

class ConfigUseCases:
    meliApi = MeLiApi()
    def __init__(self):
        pass

    def create(self, configDict = {}):
        self.meliApi.api  = configDict['api']
        self.meliApi.consumer = configDict['consumer']

    def toString(self):
        return "API = {} -- CONSUMER = {}".format(self.meliApi.api, self.meliApi.consumer )