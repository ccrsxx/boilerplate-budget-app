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
        return False

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.spent += amount
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
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

def create_spend_chart(categories):
    down_space = f'{"":4}'
    up = 'Percentage spent by category\n'
    mid = first_mid = end_mid = down = end_down = ''
    all_spent = sum([cat.spent for cat in categories])
    all_percentage = {cat.category: cat.spent / all_spent * 100 for cat in categories}
    for i in reversed(range(0, 101, 10)):
        first_mid = f'{i:>3}|'
        end_mid = ''
        for cat in all_percentage:
            if all_percentage[cat] >= i:
                val = 'o'
            else:
                val = ''
            end_mid += f'{val:^3}'
        mid += f'{first_mid}{end_mid} \n'
    mid_line = f'{down_space}{"-" * (len(categories) * 3 + 1)}\n'
    words_array = [i.category.split() for i in categories]
    max_word = max([len(i.category) for i in categories])
    for i in range(max_word):
        end_down = ''
        for word in words_array:
            if len(word[0]) > i:
                val = word[0][i]
            else:
                val = ''
            end_down += f'{val:^3}'
        if i < max_word - 1:
            down += f'{down_space}{end_down} \n'
        else:
            down += f'{down_space}{end_down} '
    return f'{up}{mid}{mid_line}{down}'
