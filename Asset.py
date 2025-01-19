from abc import ABC, abstractmethod

class Asset(ABC):
    """
    Abstract base class for assets
    """
    
    # Ticker symbol
    @property
    @abstractmethod
    def ticker(self):
        pass
    
    @ticker.setter
    @abstractmethod
    def ticker(self):
        pass
    
    @ticker.deleter
    @abstractmethod
    def ticker(self):
        pass
    
    
    # ISIN number
    @property
    @abstractmethod
    def ISIN(self):
        pass
    
    @ISIN.setter
    @abstractmethod
    def ISIN(self):
        pass
    
    @ISIN.deleter
    @abstractmethod
    def ISIN(self):
        pass
    
    
    # Exchange on which asset is traded
    @property
    @abstractmethod
    def exchange(self):
        pass
    
    @exchange.setter
    @abstractmethod
    def exchange(self):
        pass
    
    @exchange.deleter
    @abstractmethod
    def exchange(self):
        pass