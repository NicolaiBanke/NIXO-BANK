from Models.Models import Model
from Portfolio import Portfolio

class CAPM(Model):
    def __init__(self, portfolio: Portfolio, RM, Rf):
        """
        portfolio: returns vector of the portfolio in question
        RM: returns
        """
        self._portfolio = portfolio
        self._RM = RM
        self._Rf = Rf

if __name__ == "__main__":
    capm = CAPM()
    print(capm)