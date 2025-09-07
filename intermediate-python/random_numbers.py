'''
Generate random numbers
- how to generate pseudo-random numbers
- use secrets module for cryptographically strong random numbers
- use numPy to generate array of random numbers
'''

import random
import secrets
import numpy as np


# Generate pseudo random float between 0 and 1
a = random.random()
print(f'print random float: {a}')


# Generate random float with specific range
a = random.uniform(0, 3)
print(f'print random float between range: {a}')


# Generate random int with specific range
a = random.randrange(-10, 10)  # this does not include upper bound
# a = random.randint(-10, 10) - this includes the upper bound
print(f'print random int between range: {a}')


# Generate random value from a normal distribution with a mean of 0 and std deviation of 1
a = random.normalvariate(0, 1)
print(f'print random value from normal distribution: {a}')


# Use random to choose an element from list
list1 = list("ABCDEFGHIJK")
print(f'one random value: {random.choice(list1)}')

# selects random items, dups are okay
print(f'random values, with dups: {random.choices(list1, k=6)}')

# selects a bunch of items from list, but will not pick duplicates
print(f'random values no dups: {random.sample(list1, 3)}')

# shuffles a list
list1 = list("ABCDEFGHIJK")
random.shuffle(list1)
print(f'random shuffling of list: {list1}')

# You can use the 'random.seed()' function to generate the same data
#   For example, the following execution will produce the same data with each execution
random.seed(1)
print(f'random float: {random.random()}')
print(f'random int: {random.randint(1, 10)}')
random.seed(5)
print(f'random float: {random.random()}')
print(f'random int: {random.randint(1, 10)}')


random.seed(1)
print(f'random float: {random.random()}')
print(f'random int: {random.randint(1, 10)}')
random.seed(5)
print(f'random float: {random.random()}')
print(f'random int: {random.randint(1, 10)}')




'''
Using random for security
- used for password, security tokens, etc
'''
print(f'\n\n<<<<<  Using secrets for security  >>>>>')

# product a random integer between 0-9
print(f'random number between 0 & 9: {secrets.randbelow(10)}')
print(f'random 4 bits: {secrets.randbits(4)}')

# this order in which the random value is selected is not replaceable
list1 = list("ABCDEFGHIJK")
print(f'random value from list: {secrets.choice(list1)}')




'''
Using numPy to generate array of random numbers
'''

print(f'\n\n<<<<<  Using numPy to generate random values  >>>>>')

# generates 1x3 array of random float values
print(f'generates random floats: {np.random.rand(3)}')

# generates 3x3 array of random float values
print(f'generates random floats: {np.random.rand(3,3)}')

# generates 1x3 array of random int values
print(f'generates random ints: {np.random.randint(0,10,3)}')

# generates 3x4 array of random int values
print(f'generates random ints: {np.random.randint(0,10,(3,4))}')

# random shuffle
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'arr: {arr}')
np.random.shuffle(arr)
print(f'shuffled arr: {arr}')