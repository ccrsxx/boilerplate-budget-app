class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.spent = 0

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
            self.spent += amount
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
            return False

    def __str__(self):
        title = f'{self.category:*^30}\n'
        items = ''
        for item in self.ledger:
            desc = item['description'][:23]
            amount = f'{item["amount"]:.2f}'[:7]
            items += f'{desc:<23}{amount:>7}\n'
        total = f'{self.get_balance():.2f}'[:7]
        return f'{title}{items}Total: {total}'

def spent_percentage(categories):
    all_percentage = {}
    all_spent = sum([cat.spent for cat in categories])
    for cat in categories:
        val = round_ten(cat.spent / all_spent * 100)
        all_percentage[cat.category] = val
    return all_percentage

def round_ten(num):
    if num % 10 < 5:
        return int(num / 10) * 10
    else:
        return int((num + 10) / 10) * 10

def create_spend_chart(categories):
    up = 'Percentage spent by category\n'
    





    return up
