class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spending = 0

    
    def deposit(self, amount,description=""):
        self.ledger.append({"amount" : amount, "description" : description})
        self.balance += amount
    
    def withdraw(self, amount,description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.spending += amount
            self.ledger.append({"amount" : -amount, "description" : description})  
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, dest):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {dest.name}')
            self.spending -= amount
            dest.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
    
    def check_funds(self,amount):
        if amount > self.balance:
            return False
        else:
            return True
    
    def __str__(self):
        title = ''
        title += self.name.center(30, '*')
        res = ''
        res += title + '\n'
        total = 0
        for i in self.ledger:
            d = i["description"][:23]
            if not 'deposit' in res:
                if 'Transfer' in i["description"]:
                    d = i["description"]
            a = f'{i["amount"]:.2f}'
            l = f'{d}' + a.rjust(len(title) - len(d)) + '\n'
            total += i["amount"]
            res += l
        t = f'Total: {total:.2f}'
        res += t
        return res
    


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
auto = Category("Auto")
food.transfer(50, clothing)
food.transfer(100, auto)
clothing.withdraw(30.50, 't-shirt')
auto.withdraw(70.30, "engine")

print(food)
print(auto)
print(clothing)
