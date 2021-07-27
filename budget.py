class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        print(self.category, 'created')

    def deposit(self, amount, description=None):
        self.ledger.append({"amount": amount, "description": description})
        print(f'{self.ledger[0]["amount"]}$ deposited {self.ledger[0]["description"]!r}')

    def check_funds(self, amount):
        if self.ledger[0]['amount'] >= amount:
            return True
        else:
            return False

    def withdraw(self, amount, description=None):
        if self.check_funds(amount):
            self.ledger[0]['amount'] -= amount
            print(f'{"%.2f" % self.ledger[0]["amount"]}$ left -{amount}$ {description!r}')
            return True
        else:
            print(f'Not enough money to buy {description}')
            return False

    def get_balance(self):
        print(f'{self.ledger[0]["amount"]}$ {self.category}\'s money now')
        return self.ledger[0]['amount']

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            print(f'Not enough money to transfer to {category.category}')
            return False
        

# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

emilia = Category('Emilia')
emilia.deposit(100, 'by emilia')
emilia.withdraw(40, 'buying keyboard')
emilia.get_balance()

rem = Category('Rem')
emilia.transfer(60, rem)

emilia.get_balance()
rem.get_balance()

# for i in waifu.ledger:
#     print(i['description'], i['amount'])
# print('deposit', waifu.ledger[0]['amount'])
# print('desc', waifu.ledger[0]['description'])

# print('deposit', waifu.ledger[0]['amount'])