# Lists: collection data type that is ordered, mutable, and allows duplicate elements

# creating a list & adding values
mylist = ["apple", "grapefruit", "banana", "cherry", "mango"]
print(mylist)

# create an empty list
mylist2 = list()
print(mylist2)  # prints empty list

# list can contain different data types
mylist2 = [5, True, 'grass', 5]
print(mylist2)

# accessing individual elements (zero-based index)
item = mylist[0]
print(item)

# access last item in list
print(mylist[-1])

# iterating over loop
for i in mylist:
  print(i, end=',')

# check if item is in list
if 'banana' in mylist:
  print('banana is in list')
else:
  print('banana is not in list')

# elements in list
print(len(mylist))

# append items to list
mylist.append('lemon')
print(mylist)

# insert items at a specific location
mylist.insert(1, 'watermelon')
print(mylist)

# remove the last item & returns it
item = mylist.pop()
print(item)
print(mylist)

# remove a specific element
mylist.remove('grapefruit')
print(mylist)

# remove all elements
mylist2.clear()

# reverse list
print(mylist.reverse())

# sort list - changes original list
mylist = [3, 5, 2, 7, -2, -4, 8]
# mylist.sort()
print(mylist)

# sort list - creates a new sorted list
new_sorted_list = sorted(mylist)
print(new_sorted_list)

# create a list with same values
mylist = [0] * 5
print(mylist)

# concat lists
concat_list = mylist + new_sorted_list
print(concat_list)

# slicing - a way to access sub lists
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = mylist[1:4]  #specify start & stop index - does not include the last index
print(a)

# if a start index is not present, then it starts at the beginning
a = mylist[:6]

# if an end index is not present, then it goes until the end
a = mylist[3:]

# slicing - step value - skips 2 indexes
a = mylist[1:8:2]
print(a)

# a negative step index starts the array backwards
a = mylist[::-2]
print(a)

# reverse a list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
rev_list = mylist[::-1]
print(rev_list)

# copying a list - the following method copies the address of the first list into second. So they both point to the same
#   list. Modifying one will modify the other.
list_orig = ["banana", "cherry", "mango", "apple"]
list_copy = list_orig
list_copy.append("grapefruit")
list_orig.append("pineapple")
print(list_orig)
print(list_copy)

# actual or deep copy of a list
list_orig = ["banana", "cherry", "mango", "apple"]
list_copy = list_orig.copy()
list_copy.append("grapefruit")
list_orig.append("pineapple")
print(list_orig)
print(list_copy)

# copy using list() - makes a copy of the list
list_copy = list(list_orig)

# copy using slicing - also makes a copy of the list
list_copy = list_orig[:]

# list comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
b = [i*i for i in a]
print(b)

# convert a tuple to list
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
mylist = list(tuple1)
print(mylist)