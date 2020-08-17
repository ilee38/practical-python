#!/usr/bin/env python3

# report.py
#
# Exercise 2.4
import csv
import fileparse
import stock
import tableformat

def read_portfolio(filename):
    with open(filename) as f:
        portdicts = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float]) 
        portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return portfolio


def read_prices(filename):
    with open(filename) as f:
        return dict(fileparse.parse_csv(f, types=[str, float], has_headers=False)) 


def make_report(portfolio, prices):
    updated_portfolio = []

    for holding in portfolio:
        name = holding.name
        shares = int(holding.shares)
        price = prices[name]
        change = price - float(holding.price)
        updated_portfolio.append((name, shares, price, change))

    return updated_portfolio


def print_report(reportdata, formatter):
     formatter.headings(['Name','Shares','Price','Change'])
#     headers = ('Name', 'Shares', 'Price', 'Change')
#     separator = '----------'
#     print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
#     print(f'{separator:>10s} {separator:>10s} {separator:>10s} {separator:>10s}')
     for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
#    currency_sym = '$'
#    for name, shares, price, change in report:
#        money = f'{currency_sym}{price:0.2f}'
#        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report = make_report(portfolio, prices)


    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    portfolio_report(argv[1], argv[2], argv[3])


if __name__ == '__main__':
    import sys
    main(sys.argv)
