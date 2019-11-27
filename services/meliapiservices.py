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