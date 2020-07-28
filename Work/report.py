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
            record = dict(zip(headers, row))
            holding = record
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


def make_report(portfolio, prices):
    updated_portfolio = []

    for holding in portfolio:
        name = holding['name']
        shares = int(holding['shares'])
        price = prices[name]
        change = price - float(holding['price'])
        updated_portfolio.append((name, shares, price, change))

    return updated_portfolio


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    separator = '----------'
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{separator:>10s} {separator:>10s} {separator:>10s} {separator:>10s}')

    currency_sym = '$'
    for name, shares, price, change in report:
        money = f'{currency_sym}{price:0.2f}'
        print(f'{name:>10s} {shares:>10d} {money:>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')