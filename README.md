Coingecko
Requirements
Requires python3 and requests library.

pip install requests
Installation
install script
Clone the repository.

git clone https://github.com/M0nero/Coingecko.git
cd Coingecko
edit path in the script
Provide proper path to the file where data will be saved. You need to edit test.py file. In my case it is:

sys.path.insert(0, '/Users/gorda/Desktop/PyProjects/ass1/src')
Usage
# after installing the project and changing path
cd Coingecko\test
python test.py
Examples
You need just input a number of top N cryptocurrencies which are sorted by market capitalization.

Usage example:
Enter the number of displayed cryptocurrencies (1...250) : 7

1 Bitcoin     
2 Ethereum    
3 Cardano     
4 Tether      
5 Binance Coin
6 XRP
7 Solana