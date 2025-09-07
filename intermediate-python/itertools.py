# itertools: module to handle iterators with advance features like product, permutations,
#   combinations, accumulate, groupby, and infinite iterators

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

'''
=========================================================
Product Iterator
- compute the cartesian product of an iterables
=========================================================
'''
print('<<<<<<<<<<   Product Iterator   >>>>>>>>>>')

list1 = [1, 2]
list2 = [6, 7]
prod = product(list1, list2, repeat=2)
print(list(prod))



'''
=========================================================
Permutations Iterator
- returns all possible ordering of the inputs items
=========================================================
'''
print('\n<<<<<<<<<<   Permutations Iterator   >>>>>>>>>>')

list1 = [1, 2, 3, 4]
print(f'possible permutations: {list(permutations(list1))}')

# length of the permutations can be specified. This will print out permutations of only
#   2 items
print(f'length of permutations: {list(permutations(list1, 2))}')



'''
=========================================================
Combinations Iterator
- makes all possible combinations with a specified length
=========================================================
'''
print('\n<<<<<<<<<<   Combinations Iterator   >>>>>>>>>>')

list1 = [1, 2, 3, 4]
comb = combinations(list1, 2)
print(f'combinations: {list(comb)}')

'''
Difference between permutations and combinations
eg: {1, 2} and {2, 1} are two different permutations but only one combination
'''

# combinations with replacements will print out duplicate elements
list1 = [1, 2, 3, 4]
comb_wr = combinations_with_replacement(list1, 2)
print(f'combination with replacements: {list(comb_wr)}')



'''
=========================================================
Accumulate Iterator
- returns accumulated sums of input
- how it works?
  - the first element remains the same
  - sum(e1 + e2) => se2
  - sum(se2 + e3) => se3
  - and so on 
- it takes each element and adds it to the accumulated sum of all previous elements 
=========================================================
'''
print('\n<<<<<<<<<<   Accumulate Iterator   >>>>>>>>>>')

list1 = [1, 2, 3, 4]
accum = accumulate(list1)
print(f'       orig list: {list1}')
print(f'accumulated sums: {list(accum)}')

# override the default 'sum' with 'multiply'
accum = accumulate(list1, func=operator.mul)
print(f'after multiplying: {list(accum)}')



'''
=========================================================
GroupBy Iterator
- returns keys and groups from an iterable
- the results are a collection of groups of numbers that occur consecutively
=========================================================
'''
print('\n<<<<<<<<<<   GroupBy Iterator   >>>>>>>>>>')

def smaller_than(x):
    return x < 10

# in the example below, it will return consecutive groups
#   where the numbers are < 10
list1 = [1, 2, 5, 10, 8, 21, 6, 3, 4, 18, 12]
group_obj = groupby(list1, key=smaller_than)
print(f'groups less than 10...')
for k, g in group_obj:
  print(k, list(g))


# another example
people_arr = [
  {'name': 'Tim', 'age': 25},
  {'name': 'Dan', 'age': 27},
  {'name': 'Lisa', 'age': 24},
  {'name': 'Claire', 'age': 28},
  {'name': 'George', 'age': 26}
]
people_grp = groupby(people_arr, key=lambda x: x['age'] < 26)
print('people groups less than age 26...')
for k, g in people_grp:
  print(k, list(g))



'''
=========================================================
Infinite Iterator
- 
=========================================================
'''
print('\n<<<<<<<<<<   Infinite Iterator   >>>>>>>>>>')

# creates an ininite loop starting at 10 & incrementing by 1
print('-- count iterator --')
for i in count(10):
  print(i)
  if i == 15:
    break

# cycle() infinitely through an iterable
print('\n-- cycle iterator --')
list1 = [1, 2, 3, 4]
cntr = 0
for i in cycle(list1):
  print(i)
  if i == 4:
    cntr += 1
  if cntr == 4:
    break

# repeat() - repeats infinitely - 2nd arg is the # of times to loop
print('\n-- repeat iterator --')
list1 = [1, 2, 3, 4]
for i in repeat(list1, 3):
  print(i)