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
    def __str__(self):
        tittle= f"{self.name:*^30}\n"
        line=""
        for idx in self.ledger:
            des=idx["description"][0:23]
            amt=f"{idx["amount"]:.2f}"
            line+=f"{des:<23}{amt:>7}\n"
        total=f"Total: {self.get_balance():.2f}\n"
        return tittle+line+total