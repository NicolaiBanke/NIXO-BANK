from Asset import Asset

class Equity(Asset):
    def __init__(self, ticker: str, ISIN: str, exchange: str):
        self._ticker = ticker
        self._ISIN = ISIN
        self._exchange = exchange
    
    @property
    def ticker(self):
        return self._ticker
    
    @property
    def ISIN(self):
        return self._ISIN
    
    @property
    def exchange(self):
        return self._exchange
    
    def __repr__(self):
        return f"Ticker: {self._ticker}, ISIN: {self._ISIN}, Exchange: {self._exchange}"

if __name__ == "__main__":
    msft = Equity("MSFT", "DK1234", "NASDAQ")
    print(msft)