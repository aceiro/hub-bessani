import requests
import json
from usecases.configusecases import ConfigUseCases

class MeLiApiService:
    def __init__(self):
        pass

    def sites(self, useCase = ConfigUseCases()):
        response = {}
        try:
            endpoint = str(useCase.meliApi.api['endpoint'])
            routeSites = str(useCase.meliApi.api['sites'])
            site_id = str(useCase.meliApi.api['site_id'])
            routeSites = routeSites.replace("${ENDPOINT}", endpoint)
            routeSites = routeSites.replace("${SITE_ID}", site_id)
            message = json.dumps(requests.get(routeSites).text, indent=4, sort_keys=True)
            response['status']  = 200
            response['message'] = message
        except:
            response = {'status':500, 'message': 'Fail request'}
            print("Error to process URL")
        return response