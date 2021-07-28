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
        total = f'{self.get_balance():.2f}'[:7]
        object = f'{title}{items}Total: {total}'
        return object

def truncate(num, decimals=0):
    multiplier = 10 ** decimals
    return int(num * multiplier) / multiplier

def spent_percentage(categories):
    all_percentage = {}
    all_spent = sum([cat.spent for cat in categories])
    for cat in categories:
        val = truncate((cat.spent / all_spent * 100), -1)
        all_percentage[cat.category] = val
    return all_percentage

def create_spend_chart(categories):
    mid = first_mid = end_mid =''
    down = first_down = end_down = ''
    all_percentage = spent_percentage(categories)
    up = 'Percentage spent by category\n'
    for i in reversed(range(0, 101, 10)):
        first_mid = f'{i:>3}|'
        end_mid = ''
        for cat in all_percentage:
            if all_percentage[cat] >= i:
                val = 'o'
            else:
                val = ''
            end_mid += f'{val:^3}'
        mid += (f'{first_mid}{end_mid}\n')
    mid_line = f'{"":4}{"-" * (len(categories) * 3 + 1)}\n'
    words_array = [i.split() for i in all_percentage]
    max_word = max([len(i) for i in all_percentage])
    for i in range(max_word):
        end_down = ''
        for word in words_array:
            if len(word[0]) > i:
                val = word[0][i]
            else:
                val = ''
            end_down += f'{val:^3}'
        down += f'{"":4}{first_down}{end_down}\n'
    chart = f'{up}{mid}{mid_line}{down}'
    return chart
