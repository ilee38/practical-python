#!/usr/bin/env python3

# report.py
#
# Exercise 2.4
import csv
import fileparse
import stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename, **opts):
    with open(filename) as f:
        portfolio = Portfolio.from_csv(f)
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
     for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


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
