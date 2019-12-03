import requests
import json
from usecases.configusecases import ConfigUseCases
from services.servicebase import ServiceBase

class MeLiApiService(ServiceBase):
    def __init__(self):
        pass

    def categories(self, useCase = ConfigUseCases()):
        routeCategories = str(useCase.meliApi.api['categories'])
        return self.buildRouteAndGetHttp(useCase, routeCategories)

    def sites(self, useCase = ConfigUseCases()):
        routeSites = str(useCase.meliApi.api['sites'])
        return self.buildRouteAndGetHttp(useCase, routeSites)

    def catalogListByQuery(self, useCase = ConfigUseCases()):
        routeSites = str(useCase.meliApi.api['catalog_listing'])
        query = "Motorola"

        response = self.buildRouteAndGetHttp(useCase, routeSites, query)
        response_api  = json.loads(response["response_api"])
        results       = response_api['results']
        products = []
        for item in results:
            price = item['price']
            description = r''.join(item['title']).encode('utf-8').strip()
            product = {}
            product['price'] = price
            product['description'] = description
            products.append(product)        
        return products