import requests as req
import dotenv
import os

dotenv.load_dotenv()

class Saxo:
    def __init__(self):
        _bearer_token = os.getenv('SAXO_BEARER_TOKEN')
        self._base_url = "https://gateway.saxobank.com/sim/openapi"
        self._headers = {
            "Authorization": f"Bearer {_bearer_token}"
            }
    
    @property
    def base_url(self):
        return self._base_url
    
    @property
    def headers(self):
        return self._headers
    
    def get(self, path=""):
        res = req.get(self.base_url + path, headers=self.headers)
        return res.json()
    
    def post(self, path="", body={}):
        res = req.post(self.base_url + path, data=body)
        return res.json()