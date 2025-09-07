# Tuples: collection data type which is ordered, immutable, and allows duplicate elements
#   A tuple CANNOT be updated after creation

import sys
import timeit

# creating a tuple - parenthesis are optional but good practice
tuple1 = ('max', 28, 'Chicago')
print(tuple1)

# a single value as tuple is not recognized. The following line with create a string
#  to create a tuple use this -> ('max',)
tuple1 = ('max',)
print(type(tuple1))

# create a tuple from list
list1 = ['mango', 1, 5, 'airplane']
tuple1 = tuple(list1)
print(tuple1)

# accessing elements inside tuple - use indexes to access the data
#   a negative index follows the same rules as lists
print(tuple1[0])

# loop over all elements in a tuple
for i in tuple1:
    print(i)

for n, i in enumerate(tuple1):
    print(f'value:{n}-index:{i}', end='|')

# check for an element in tuple
if 'mango' in tuple1:
  print('yes')
else:
  print('no')

# get number of elements in tuple
print(len(tuple1))

# get occurrences of elements in tuple
tuple1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'b', 'c', 'a', 'b', 'c')
print(tuple1.count('a'))

# find first occurring index - if an element doesn't exist in the tuple, the following will
#  throw an error
print(tuple1.index('a'))

# slicing tuples - works the same way as in lists - returns a new tuple
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print(tuple1[2:4])

# to reverse a tuple
rev_tuple1 = tuple1[::-1]
print(rev_tuple1)

# unpacking a tuple
tuple1 = ('mango', 28, 'Chicago')
name, age, city = tuple1     # number of variables MUST match the # of element in tuple
print(f'{name} is {age} years old in {city}')

# unpack multiple elements using '*'
tuple1 = (1,2,3,4,5,6,7,8,9,10)
i1, *i2, i3 = tuple1     # i1 gets first item, i3 gets last item, and the '*' create a new list of items in the middle
print(i1, i2, i3)

# compare a tuple & list when working with large data
#   tuples are more efficient than a list
list1 = [0, 1, 2, 'hello', True]
tuple1 = (0, 1, 2, 'hello', True)
print(sys.getsizeof(list1), 'bytes')
print(sys.getsizeof(tuple1), 'bytes')

# check the execution time - below we are executing a statement 1M times and timing it
print(timeit.timeit(stmt='[0,1,2,3,4,5]', number=1000000))
print(timeit.timeit(stmt='(0,1,2,3,4,5)', number=1000000))

