# https://python.swaroopch.com/data_structures.html

# Variables

x=5
y='Orange'
z=True


## List [ , ]
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

## Tupple ( , )

# I would recommend always using parentheses
# to indicate start and end of tuple
# even though parentheses are optional.
# Explicit is better than implicit.

# Tuples are used to hold together multiple objects. 
# Think of them as similar to lists, but without the 
# extensive functionality that the list class gives you. 
# One major feature of tuples is that they are immutable 
# like strings i.e. you cannot modify tuples.

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo    # parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))



#Tuple with 0 or 1 items

# An empty tuple is constructed by an empty pair of parentheses 
# such as myempty = (). However, a tuple with a single item 
# is not so simple. You have to specify it using a comma 
# following the first (and only) item so that Python can 
# differentiate between a tuple and a pair of parentheses 
# surrounding the object in an expression
#  i.e. you have to specify singleton = (2 , )
#  if you mean you want a tuple containing the item 2.

## Dictionary {key:value,}

# A dictionary is like an address-book where you can find the address 
# or contact details of a person by knowing only his/her name 
# i.e. we associate keys (name) with values (details). 
# Note that the key must be unique just like you cannot find out 
# the correct information if you have two persons with the exact same name.

# 'ab' is short for 'a'ddress'b'ook

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

## Sequence [ , ]

# Lists, tuples and strings are examples of sequences, 
# but what are sequences and what is so special about them?
# The major features are membership tests, (i.e. the in and not in expressions) 
# and indexing operations, which allow us to fetch a particular item in 
# the sequence directly.
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

## Set set( [ , ] )

# Sets are unordered collections of simple objects. 
# These are used when the existence of an object in a collection 
# is more important than the order or how many times it occurs.
# Using sets, you can test for membership, whether it is a subset 
# of another set, find the intersection between two sets, and so on.

bri = set(['brazil', 'russia', 'india'])
'india' in bri

'usa' in bri

bric = bri.copy()
bric.add('china')
bric.issuperset(bri)

bri.remove('russia')
bri & bric # OR bri.intersection(bric)
