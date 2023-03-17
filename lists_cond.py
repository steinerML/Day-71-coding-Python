#Lists: Conditional tests

#Testing if a value is in a list
players = ['alice', 'bea', 'dennis', 'debbie']

print('bea' in players)

#Remove instances of a list

pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']

print(pets)

#We remove cat from the list
pets.remove('cat')
print(pets)

#We now re-insert it again
pets.insert(1,'cat')
print(pets)

#We remove ALL cats from the list

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#Passing a List to a function

def greet_users(names):
    """We run a loop through a List"""
    for name in names:
        print('Hello!', name)

names = ['Peter', 'Fiona', 'Steven', 'Nicole']
greet_users(names)
