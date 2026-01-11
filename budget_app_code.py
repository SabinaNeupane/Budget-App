class Category():
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self,amt,description):
        self.ledger.append({'amount':amt,'description':description})
    def withdraw(self,amt,description):
        self.ledger.append({'amount':-amt,'description':description})