#!/usr/bin/env python3

# pcost.py
#
# Exercise 1.27
import sys
import report

def portfolio_cost(filename):
    total_cost = 0.0
    stock_price = 0.0
    num_of_shares = 0
    records = report.read_portfolio(filename) 

    for lineno, record in enumerate(records, start=1):
        try:
            nshares = int(record.shares)
            price = float(record.price)
            total_cost += nshares * price
        # This catches errors in int() and float() conversions above
        except ValueError:
            print(f'Row {lineno}: Bad row: {line}')
            
    return total_cost

def main(argv):
    if len(argv) == 2:
       filename = argv[1]
    else:
     filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)
    
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
