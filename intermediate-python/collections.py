# Collections: provide additional containers: Counter, Named Tuple, Ordered Dictionary, Default Dictionary, Deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

'''
=========================================================
Counter collection
- stores the elements as keys and counts as values
=========================================================
'''
print('<<<<<<<<<<   Counter Collection   >>>>>>>>>>')

a = 'aaaaaabbbbcccddefffff'
counter1 = Counter(a)
print(f'counter items: {counter1.items()}')
print(f'counter keys: {counter1.keys()}')
print(f'counter values: {counter1.values()}')
print(f'most common items: {counter1.most_common()}')   # will return a list with tuple
print(f'one most common items: {counter1.most_common(1)}')
print(f'two most common items: {counter1.most_common(2)}')

# show most common element
print(f'most common element: {counter1.most_common(1)[0][0]}')

# returns all the different elements as single list elements
print(f'list of elements * count: {list(counter1.elements())}')



'''
=========================================================
Named Tuple collection
- lightweight object type similar to struct
=========================================================
'''
print('\n<<<<<<<<<<   Named Tuple Collection   >>>>>>>>>>')

# 1st arg: class name (typically same as var name)
# 2nd arg: all the fields separated by comma or space
Point = namedtuple('Point', 'x y')
pt = Point(1, 2)
print(pt)



'''
=========================================================
Ordered Dictionary collection
- keeps track of the order in which items are added to a dictionary
- NOTE: since python 3.7, the built-in dictionary does the same thing
=========================================================
'''
print('\n<<<<<<<<<<   Ordered Dictionary Collection   >>>>>>>>>>')

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['c'] = 3
ordered_dict['b'] = 2
print(ordered_dict)



'''
=========================================================
Default Dictionary collection
- similar to dictionary except that it will insert a default value for
    any unset keys
=========================================================
'''
print('\n<<<<<<<<<<   Default Dictionary Collection   >>>>>>>>>>')

default_dict = defaultdict(int)  # can also use list instead of int
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict['c'])   # will return a default value instead of an error



'''
=========================================================
Deque collection
- double ended queue - add/remove elements from both ends
=========================================================
'''
print('\n<<<<<<<<<<   Deque Collection   >>>>>>>>>>')

d = deque(['a', 'b', 'c'])
d.append('d')
d.append('e')
print(f'append: {d}')

d.appendleft('f')
print(f'append left: {d}')

d.pop()
print(f'pop: {d}')

d.popleft()
print(f'pop left: {d}')

d.extendleft(['g', 'h'])
print(f'extend left: {d}')

# move elements to right - last element moves to front
d.rotate(1)
print(f'after rotating 1 place to right: {d}')

# move elements to left - first element moves to end
d.rotate(-1)
print(f'after rotating 1 place to left: {d}')