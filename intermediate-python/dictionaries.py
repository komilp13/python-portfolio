# Dictionary: collection data type, key-value pairs, unordered, mutable

# creation
dict1 = {'name': 'Tim', 'age': 24, 'city': 'Dallas'}
print(dict1)

# creation using dict() function
dict2 = dict(name='Mary', age=23, city='Chicago')
print(dict2)

# accessing values - if a key doesn't exist, there will be an error
value = dict2['name']
print(value)

# adding item to dict
dict2['email'] = 'test@test.com'
print(dict2)

# updating an item in dictionary
dict2['email'] = 'nice.test@test.com'
print(dict2)

# deleting items from dictionary
del dict2['email']
# dict2.pop('email')
# dict2.popitem()     # removes the last inserted item
print(dict2)

# check if key exists
if 'email' in dict2:
  print(dict2['email'])
else:
  print('no key')

# looping through a dictionary
for key, value in dict2.items():
  print(key, value)

# loop through all the keys
for key in dict2.keys():
  print(key)

# loop over the values
for value in dict2.values():
  print(value)

# copying a dictionary - creates a point to original
dict1_copy = dict1

# deep copy
dict1_copy = dict1.copy()
dict1_copy = dict(dict1)

# merge dictionary - in the following method, all the existing keys are overwritten with the
#   incoming values. Any new keys are added
dict1 = {'name': 'Tim', 'age': 24, 'email': 'tim@email.com'}
dict2 = dict(name='Mary', age=23, city='Chicago')
dict1.update(dict2)
print(dict1)

# key types - can use any immutable types, even tuples
#   List CANNOT be a key since it is mutable
tuple1 = (1, 2, 3)
dict1 = { tuple1: (4,5,6)}
print(dict1)