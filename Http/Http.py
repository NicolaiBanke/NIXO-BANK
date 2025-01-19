from typing import Protocol

class Http(Protocol):
    """
    Protocol for implementing HTTP requests to the external APIs such as from saxo, or financial databases, etc.
    """

    def get(self, path: str) -> dict:
        ...
    
    def post(self, path: str, body) -> dict:
        ...
    
    def delete(self) -> dict:
        ...
    
    def put(self) -> dict:
        ...