from Http.Http import Http
from utils.APIEndpoint import APIEndpoint

class Positions(APIEndpoint):
    def __init__(self, imp: Http):
        self._imp = imp
        self._endpoint = '/port/v1/positions'
    
    @property
    def imp(self):
        return self._imp
    
    @property
    def endpoint(self):
        return self._endpoint
    
    def get_client_positions(self):
        res = self.imp.get(self.endpoint + "/me")
        return res