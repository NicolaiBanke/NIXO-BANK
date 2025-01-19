from abc import ABC, abstractmethod

class APIEndpoint(ABC):
    """
    Abstract base class for the API-endopints handled by the implementations of the HTTP protocol.
    An implementation must have a property called 'imp', the specific implementation
    of the HTTP protocol and a property called 'endpoint', the basic API-endpoint on which
    the requests are mounted
    """
    
    @property
    @abstractmethod
    def imp(self):
        pass
    
    @property
    @abstractmethod
    def endpoint(self):
        pass