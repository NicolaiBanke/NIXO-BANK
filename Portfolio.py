from Asset import Asset
from Equity import Equity
from ETF import ETF

class Portfolio:
    def __init__(self, assets: list[Asset]):
        self.assets = assets
    
    def __repr__(self):
        asset_list = ""
        for asset in self.assets:
            asset_list += f"{asset}\n"
        
        return asset_list



if __name__ == "__main__":
    msft = Equity("MSFT")
    spy = ETF("SPY")
    portfolio = Portfolio([msft, spy])
    
    print(portfolio)