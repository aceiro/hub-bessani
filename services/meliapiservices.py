import requests
import json
from usecases.configusecases import ConfigUseCases

class ServiceBase:
    def __init__(self):
        pass
    def buildRouteAndGetHttp(self, useCase = ConfigUseCases(), routeApi = ""):
        response = {}
        try:
            endpoint = str(useCase.meliApi.api['endpoint'])            
            site_id  = str(useCase.meliApi.api['site_id'])
            routeApi = routeApi.replace("${ENDPOINT}", endpoint)
            routeApi = routeApi.replace("${SITE_ID}", site_id)
            #######################################
            # chama ML API remota
            #######################################
            categories = requests.get(routeApi).text
            
            #######################################
            # monta o json
            #######################################
            message = json.dumps(categories, sort_keys=True)            
            response['status']  = 200
            response['message'] = message
        except:
            response = {'status':500, 'message': 'Fail request'}
            print("Error to process URL")
        return response

class MeLiApiService(ServiceBase):
    def __init__(self):
        pass

    def categories(self, useCase = ConfigUseCases()):
        routeCategories = str(useCase.meliApi.api['categories'])
        return self.buildRouteAndGetHttp(useCase, routeCategories)

    def sites(self, useCase = ConfigUseCases()):
        routeSites = str(useCase.meliApi.api['sites'])
        return self.buildRouteAndGetHttp(useCase, routeSites)