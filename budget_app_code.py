class Category():
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self,amt,description):
        self.ledger.append({'amount':amt,'description':description})
    def withdraw(self,amt,description):
        self.ledger.append({'amount':-amt,'description':description})
    def get_balance(self):
        bal=0
        for idx in self.ledger:
            bal=bal+idx["amount"]
        return bal
    def transfer(self,amt,u2):
        self.ledger.append({'amount':-amt,'description':f"Transfer to {u2.name}"})
        u2.ledger.append({'amount':amt,'description':f"Transfer from {self.name}"})
    def check_funds(self,amt):
        return amt<=self.get_balance()