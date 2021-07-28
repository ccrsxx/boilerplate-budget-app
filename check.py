x = [
    {'amount': 55, 'description': 'by emilia'}, 
    {'amount': 40, 'description': 'buying keyboard'}, 
    {'amount': 20, 'description': 'buying novel'}, 
    {'amount': 25, 'description': 'get a vaccine'}, 
    {'amount': 60, 'description': 'Transfer to Rem'}
]

print(len(x))

for i in x[1:]:
    amount = i['amount']
    desc = i['description']
    print(amount, desc)