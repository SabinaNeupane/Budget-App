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
    
def create_spend_chart(categories):
    spent = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)
    percentages = [(s / total_spent) * 100 for s in spent]
    rounded = [int(p // 10 * 10) for p in percentages]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for p in rounded:
            chart += " o " if p >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        chart += "\n"

    return chart.rstrip("\n")