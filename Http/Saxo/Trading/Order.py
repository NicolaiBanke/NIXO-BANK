from Http.Http import Http
from utils.APIEndpoint import APIEndpoint

class Order(APIEndpoint):
    """
    End points for placing, changing and canceling orders.
    """

    def __init__(self, imp):
        self._imp = imp
        self._endpoint = '/trade/v2/orders'
    
    @property
    def imp(self):
        return self._imp
    
    @property
    def endpoint(self):
        return self._endpoint
    
    def place_new_order(self, order):
        """
        The order can contain optional limit and stop orders, by adding them as child orders.
        It is also possible to place an order on behalf of another client (for IBs).
        The account key property of the order determines the client account on which the order is placed.
        """
        res = self.imp.post(self.endpoint, order)
        return res