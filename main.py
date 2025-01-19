from Http.Saxo.Saxo import Saxo
from Http.Saxo.Portfolio.Balances import Balances
from Http.Saxo.Portfolio.Positions import Positions

if __name__ == "__main__":
    balances = Balances(Saxo())
    client_balance = balances.get_client_balance()
    positions = Positions(Saxo())
    client_positions = positions.get_client_positions()
    print(client_positions)