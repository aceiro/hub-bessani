from usecases.configusecases import ConfigUseCases
from services.meliapiservices import MeLiApiService
import time
class HubController:
    def __init__(self):
        pass
    def printCsv(self, products = []):
        for product in products:
            print("{},{}".format(product['price'], product['description']))

    def startMainLoop(self, configDict):
        iteration = 1
        while 1==1:
            useCases = ConfigUseCases()
            useCases.create(configDict)
            print("#{} Main HUB loop started".format(iteration))
            print("# Config HUB -- {}".format(useCases.toString()))

            print("# Starting service - sites")
            servicesApi = MeLiApiService()
            for service in configDict['services']:
                if service == "sites":
                    response = servicesApi.sites(useCases)
                elif service == "categories":
                    response = servicesApi.categories(useCases)
                elif service == "catalog_listing":
                    response = servicesApi.catalogListByQuery(useCases)
                    self.printCsv(response)
                #print("# Starting {}".format(service))      
                #print("# Service HUB -- {}".format(response))

            iteration = iteration + 1
            time.sleep(5)
