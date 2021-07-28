class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        print(self.category, 'created')

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance = self.ledger[0]['amount']
        print(f'{self.ledger[0]["amount"]}$ deposited {self.ledger[0]["description"]!r}')

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            print(f'{"%.2f" % self.ledger[0]["amount"]}$ left -{amount}$ {description!r}')
            return True
        else:
            print(f'Not enough money to buy {description}')
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            print(f'Not enough money to transfer to {category.category}')
            return False

    def __str__(self):
        title = f'{self.category:*^30}\n'
        items = ''
        for item in self.ledger:
            desc = item['description'][:23]
            amount = f'{item["amount"]:.2f}'[:7]
            items += f'{desc:<23}{amount:>7}\n'
        total = str(self.get_balance())[:7]
        return f'{title}{items}Total: {total}'




food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

emilia = Category('Emilia')
emilia.deposit(200, 'by emilia')
emilia.withdraw(69.69, 'buying keyboard')
emilia.withdraw(20, 'buying novel')
emilia.withdraw(25, 'get a vaccine')
emilia.get_balance()

rem = Category('Rem')
emilia.transfer(60, rem)

emilia.get_balance()
rem.get_balance()

print(clothing)
print(auto)
print(food)