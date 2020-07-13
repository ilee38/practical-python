# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    cost = 0.0
    stock_price = 0.0
    num_of_shares = 0
    f = open(filename, 'rt')
    headers = next(f)

    for line in f:
        try:
            stock = line.split(',')
            num_of_shares = int(stock[1])
            stock_price = float(stock[2].strip())
            cost += (num_of_shares * stock_price)
        except ValueError:
            print('Bad line', line)
            
    f.close()
    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)