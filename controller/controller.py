from usecases.configusecases import ConfigUseCases
from services.meliapiservices import MeLiApiService
import time
class HubController:
    def __init__(self):
        pass
    
    def startMainLoop(self, configDict):
        iteration = 1
        while 1==1:
            useCases = ConfigUseCases()
            useCases.create(configDict)
            print("#{} Main HUB loop started".format(iteration))
            print("# Config HUB -- {}".format(useCases.toString()))

            print("# Starting service - sites")
            servicesApi = MeLiApiService()
            response = servicesApi.sites(useCases)
            print("# Service HUB -- {}".format(response))

            print("# Starting service - categories")

            response = servicesApi.categories(useCases)
            print("# Service HUB -- {}".format(response))

            iteration = iteration + 1
            time.sleep(5)