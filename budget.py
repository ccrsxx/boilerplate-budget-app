class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=None):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, )

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

anime = Category('naruto')
anime.deposit(10, 'pussy')

for i in anime.ledger:
    print(i['description'], i['amount'])
print('deposit', anime.ledger[0]['amount'])
print('desc', anime.ledger[0]['description'])