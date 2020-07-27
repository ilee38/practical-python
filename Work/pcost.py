# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    stock_price = 0.0
    num_of_shares = 0
    f = open(filename, 'rt')
    lines = csv.reader(f)
    headers = next(lines)

    for lineno, line in enumerate(lines, start=1):
        record = dict(zip(headers, line))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total_cost += nshares * price
        # This catches errors in int() and float() conversions above
        except ValueError:
            print(f'Row {lineno}: Bad row: {line}')
            
    f.close()
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)