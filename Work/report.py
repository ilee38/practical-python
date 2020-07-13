# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    prices = {}

    f = open(filename, 'rt')
    lines = csv.reader(f)
    for line in lines:
        try:
            prices[line[0]] = float(line[1])
        except IndexError:
            pass
    f.close()
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

bought_price = 0.0
curr_price = 0.0
for holding in portfolio:
    bought_price += holding['shares'] * holding['price']
    curr_price += holding['shares'] * prices[holding['name']]

print(f'Portfolio starting value {bought_price:0.2f}')
print(f'Current portfolio value {(curr_price):0.2f}')
if curr_price >= bought_price:
    print(f'Gain +{(curr_price - bought_price):0.2f}')
else:
    print(f'Loss -{abs(curr_price - bought_price):0.2f}')