# Strings: collection type, ordered, immutable, text representation

# creation
str1 = 'Test'   # or "Test"
print(str1)

# escaping quotes
str1 = 'I\'m a string' # or "I'm a string"
print(str1)

# multi-line strings
str1 = '''Hello
World'''
print(str1)

# substrings
str1 = 'Hello World'
print(str1[4])

# access string using negative index
print(str1[-2])
print(str1[:-2])
print(str1[::-1])   # reverses the string

# concat strings
print('greeting' + ' ' + 'to you')

# iterate over string
for i in str1:
  print(i, end=' ')
print()

# check for substring
if 'e' in str1:
  print('yes')
else:
  print('no')

# remove whitespaces
str1 = str1.strip()

# convert to upper/lower
print(str1.upper())
print(str1.lower())

# check string for substring
print(str1.startswith('H'))
print(str1.endswith('d'))

# find index of - returns index of first occurrence
print(str1.index('lo'))      # -1 is returned if the substr is not found

# number os occurrence of substr
print(str1.count('o'))

# replace substr
str1 = 'Hello World'
print(str1.replace('World', 'Universe'))

# convert str to list
str1 = 'how are you doing sir'
list1 = str1.split()    # default delimiter is a space. you can substitute any char like this: split(',')
print(list1)

# convert list to str
print(' '.join(list1))    # the ' ' before the join is what is added in between the list items

#
list1 = ['a'] * 6
print(''.join(list1))

# formatting string - using %
name, age, hourly_rate = 'Mary', 32, 24.5679
print('name is %s. Her age is %d. Her hourly rate is %.2f' % (name, age, hourly_rate))

# format using .format()
print('name is {0}. Her age is {1:d}. Her hourly rate is {2:.2f}'.format(name, age, hourly_rate))

# format using 'f'
print(f'name is {name}. Her age is {age:d}. Her hourly rate is {hourly_rate:.2f}')