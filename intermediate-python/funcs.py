'''
- The difference between func args vs parameters
- Positional & keyword args
- Default args
- Variable-length args (*args and **kwargs)
- Container unpacking into function args
- Local vs. global args
- Parameter passing (by value or by ref)
'''

# Difference between func args vs parameters.
#   Parameters are vars that are used when defining a function
#   Args are the actual values that are passed when calling the func
def print_names(name):   #  <- parameter of func
  print(name)

print_names('hello')   #  <- argument to func



# Positional vs Keyword args
def foo(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

foo(1, 2, 3)    #  <- positional arguments, order of args is important here
foo(arg1=4, arg2=5, arg3=6)   #  <- keyword args, order of args is not important


# Default args
def func1(arg1, arg2, arg3=4):
    print(arg1, arg2, arg3)

func1(1,2)    #  <- don't need to pass in arg3, because it's default.
# default args must also be at the end of the pqrameter list




# *args vs **kwargs
# *args - may contain any number of positional args in that var
# **kwargs - may contain any number of key:value pair args in that var
def func2(a, b, *args, **kwargs):
  print(a, b)
  for a in args:
    print(a)
  for k in kwargs:
    print(k, kwargs[k])

func2(1,2, 3,4,5,6, six=6, seven=7)



# Force keyword in args


# Unfold a list into args
def func3(a, b, c):
  print(a, b, c)

func3(*[1,2,3])    # unpack a list; args must match param list
func3(*(4,5,6))    # unpack a tuple; args must match param list

# items in dict must match param list; keys must match param name
dict1 = {'a': 1, 'b': 2, 'c': 3}
func3(**dict1)




'''
Usages of Asterisk (*) 
'''

# simple multiplication
r = 1 * 3

# power operation
r = 2 ** 4   #  <- 2 to the power of 4

# Create strings, lists or tuples with repeated elements
zeros = [0, 2] * 3
# zeros = "AB" * 3
print(zeros)

# unpacking list into vars
nums = [1, 2, 3, 4, 5]
# the following will unpack the last element into l.  All others will
#   be unpacked into a
*a, l = nums
print(a)
print(l)

# Merge iterables into a list
tuple1 = (1, 2, 3)
list1 = [4, 5, 6]
list2 = [*tuple1, *list1]
print(list2)

# Merging dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5}
mer_dict = {**dict1, **dict2}
print(mer_dict)

