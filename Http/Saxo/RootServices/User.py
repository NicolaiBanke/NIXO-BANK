from Http.Http import Http
from utils.APIEndpoint import APIEndpoint

class User(APIEndpoint):
    def __init__(self, imp: Http):
        self._imp = imp
        self._endpoint = '/root/v2/user'
    
    @property
    def imp(self):
        return self._imp
    
    @property
    def endpoint(self):
        return self._endpoint
    
    def get_info_current_user(self):
        return self.imp.get(self.endpoint)