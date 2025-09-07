'''
Generators: functions that return objects that can be iterated over. The items are generated inside the class lazily
  and only when asked for. This is the reason they are memory efficient when dealing with larger datasets
'''
import sys

print('<<<<<<<    Generators    >>>>>>>')
def generate_int():
  for i in range(20):
    yield i

print('\nSimple generator')

g = generate_int()

# generator can be used in for loops
# for i in g:
#   print(i)

# another way to iterate over
v = next(g)
print(v)

v = next(g)
print(v)

# You can use generators as input to iterable functions such as sum(), sorted()
sumss = sum(generate_int())
print(f'Sums: {sumss}')


'''
Understanding the way generators work
  - the function runs until it encounters a yield and returns a value
  - when the function is called again, it will start the function but remember the state
'''
def countdown(number):
  while number > 0:
    yield number
    number -= 1

cd = countdown(10)
for n in cd:
  print(n)




'''
Let's figure out how efficient generators are
'''
def firstn(n):
  num_arr = []
  num = 0
  while num < n:
    num_arr.append(num_arr)
    num += 1
  return num_arr

def firstn_gen(n):
  num = 0
  while num < n:
    yield num
    num += 1

print(f'    size of firstn(): {sys.getsizeof(firstn(100000))}')
print(f'size of firstn_gen(): {sys.getsizeof(firstn_gen(100000))}')



'''
Fibonacci Sequence Generator
'''
print('\nFibonacci Sequence Generator')
def fibonacci(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b

for n in fibonacci(25):
  print(n)



'''
Generator Expressions
- short-hand way to the generator functions
'''
print('\nGenerator expressions')
mygenerator = (i for i in range(10) if i % 2 == 0)
for n in mygenerator:
  print(n)

print('\nGenerator expressions to list')
mygenerator = (i for i in range(10) if i % 2 == 0)
print(list(mygenerator))