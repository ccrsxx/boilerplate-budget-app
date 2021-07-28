class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        if not self.ledger:
            self.balance = amount
        else:
            self.balance += self.ledger[-1]['amount']
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
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

def create_spend_chart(categories):
    return create_spend_chart
