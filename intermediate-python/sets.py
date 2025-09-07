# Sets: collection data type, unordered, mutable, no duplications

# creation
set1 = {1, 2, 3, 4, 5, 5, 4}
print(set1)

# create set using list
set1 = set([1, 2, 3, 4, 5, 5, 4])
print(set1)

# create using string - This will automatically create a set and will also split
#   the words into distinct values
myset = set('Hello')
print(myset)

# create an empty set
set1 = set()
print(type(set1))

# add elements
set1.add(1)
set1.add(2)
print(set1)

# remove elements
set1.remove(2)    # generates an error if an element is not found
set1.discard(3)   # removes an element, but if an element doesn't exist, it simply exists (no errors)
set1.pop()   # returns an arbitrary value and removes it from set

# remove all elements
set1.clear()

# loop over set
set1 = set([1, 2, 3, 4, 5, 5, 4])
for i in set1:
  print(i, end=',')
print()

# to check if an element is in the set
if 1 in set1:
  print('yes')
else:
  print('no')

# union of a set - combines from both sets
odds = {1, 3, 5 ,7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}
union_set = odds.union(evens)
print(union_set)

# intersection of a set - elements that exist in both sets
intersection_set = primes.intersection(odds)
print(intersection_set)

# difference of sets - elements that are in set 1 which are not in set 2
#  this is similar to left outer join
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 2, 6, 7, 8, 9, 10, 11, 12}
print(set1.difference(set2))

# also a difference of sets - excludes elements that exist in both sets & returns the rest from both lists
print(set1.symmetric_difference(set2))

# updates the set with another set
set1.update(set2)
print(set1)

# update intersection method - updates one set with values found in both sets
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 2, 6, 7, 8, 9, 10, 11, 12}
set1.intersection_update(set2)
print(set1)

# difference update method - updates set1 by removing elements found in set2
#   DOES NOT include elements from second set
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 2, 6, 7, 8, 9, 10, 11, 12}
set1.difference_update(set2)
print(set1)

# difference update method - updates set1 by removing elements found in set2
#   includes elements from second set
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 2, 6, 7, 8, 9, 10, 11, 12}
set1.symmetric_difference_update(set2)
print(set1)

# subset - does set1 contain all all elements of set2?
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 2, 3}
print(set2.issubset(set1))

# superset - are all elements of set2 exists in set1?
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 2, 3}
print(set1.issuperset(set2))

# disjoin - returns True if there are no intersecting elements in both sets
set1 = {4, 5, 6, 7, 8, 9}
set2 = {1, 2, 3}
print(set1.isdisjoint(set2))

# copying sets - follows the same rules as Lists
# set2 = set1  -> this will simply create a pointer pointing to same memory location
set2 = set1.copy()  # this will do a deep copy
set2 = set(set1)

# frozen set - immutable version of set - CANNOT be modified once created
frozen_set = frozenset([1,2,3,4])
print(frozen_set)
