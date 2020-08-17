class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


    def sell(self, qty):
       self.shares -= qty 


    def cost(self):
       return self.shares * self.price 
