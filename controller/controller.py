from usecases.configusecases import ConfigUseCases
import time
class HubController:
    def __init__(self):
        pass
    
    def startMainLoop(self, configDict):
        iteration = 1
        while 1:
            c = ConfigUseCases()
            c.create(configDict)
            print("#{} Main HUB loop started".format(iteration))
            print("# Config HUB -- {}".format(c.toString()))
            iteration = iteration + 1
            time.sleep(5)