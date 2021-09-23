#Kabken Kaiyrkeldi SE-2008
from pycoingecko import CoinGeckoAPI


def printTop():
    cg = CoinGeckoAPI()
    s = []
    dict = cg.get_coins_markets("usd")
    Input = input("Enter the number of cryptocurrencies that you want to see: ")
    N = int(Input)
    for i in range(N):
        s.append(dict[i].get("name"))
    print(s)
