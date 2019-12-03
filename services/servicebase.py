import requests
import json
from usecases.configusecases import ConfigUseCases

class ServiceBase:
    def __init__(self):
        pass
    def buildRouteAndGetHttp(self, useCase = ConfigUseCases(), routeApi = "", query = None):
        response = {}
        try:
            endpoint = str(useCase.meliApi.api['endpoint'])            
            site_id  = str(useCase.meliApi.api['site_id'])
            routeApi = routeApi.replace("${ENDPOINT}", endpoint)
            routeApi = routeApi.replace("${SITE_ID}", site_id)

            #######################################
            # verifica se existe query para ser 
            # usada
            #######################################
            if query!=None and len(query) > 0:
                routeApi = routeApi.replace("${PRODUCT_DESC}", query)


            #######################################
            # chama ML API remota
            #######################################
            response_api = requests.get(routeApi).text
            
            #######################################
            # monta o json
            #######################################
            str_message = json.dumps(response, sort_keys=True)            
            response['status']   = 200
            response['message']  = str_message
            response['response_api'] = response_api
        except:
            response = {'status':500, 'message': 'Fail request'}
            print("Error to process URL")
        return response
