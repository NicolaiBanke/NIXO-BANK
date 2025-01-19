from Http.Http import Http
from utils.APIEndpoint import APIEndpoint

class Balances(APIEndpoint):
    """
    Implementation of 
    """
    def __init__(self, imp: Http):
        self._imp = imp
        self._endpoint = '/port/v1/balances'
    
    @property
    def imp(self):
        return self._imp
    
    @property
    def endpoint(self):
        return self._endpoint
    
    #Not working yet!
    def get_balance(self, account_group_key=None, account_key=None, client_key=None, field_groups=None):
        params = "" if not (account_group_key or account_key or client_key or field_groups) else f"?AccountGroupKey={account_group_key}&AccountKey={account_key}&ClientKey={client_key}&FieldGroups={field_groups}"
        print(params)
        res = self.imp.get(self.endpoint + params)
        return res
    
    def get_client_balance(self):
        res = self.imp.get(self.endpoint + '/me')
        return res