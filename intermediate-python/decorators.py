'''
Decorators:
- decorators are a function that takes a function as an argument and extends the behavior of the
    decorated function without modifying the original function.
- allows you to add new functionality to an existing function.
- 2 types of decorators:
  - Function decorator - extend functionality without modifying the original function.
  - Class decorator - typically used to update & maintain state
'''
import functools
from curses import wrapper

print('<<<<<<   Function decorator   >>>>>>')

# decorator without arguments
def start_end_decorator(f):
  def wrapper():
    print('--- before executing function ---')
    f()
    print('--- after executing function ---')

  return wrapper

# decorator with arguments
def logging_stuff(func):

  # the functools.wraps() method preserves the name & help details of the orig func
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print('--- start logging ---')
    r = func(*args, **kwargs)
    print('--- end logging ---')
    return r

  return wrapper


# the line below decorates the function with extension
@start_end_decorator
def printName():
    print(f'name is KP')

# decorator func with an argument
def repeat(num_times):
  def repeat_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        r = func(*args, **kwargs)
      return r
    return wrapper
  return repeat_decorator

# another way to decorate a function
# associate the decorator to the executing func so the existing
#   functionality is extended
# printName = start_end_decorator(printName)

@logging_stuff
def add5(x):
  return x + 5

# decorator with args
@repeat(3)
def greeting(name):
  print(f'Hello {name}')

printName()
print(f'adding 5: {add5(4)}')

print('\n')
print(help(add5))

greeting('Jim')



# Nested decorators
print('\nNested Decorators')
@repeat(3)
def add5(x):
  return x + 5
def start_end_decorator2(f):
  @functools.wraps(f)
  def wrapper(*args, **kwargs):
    print('--- start logging ---')
    r = f(*args, **kwargs)
    print('--- end logging ---')
    return r
  return wrapper

def debug(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    args_repr = [repr(a) for a in args]
    kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
    signature = ', '.join(args_repr + kwargs_repr)
    print(f'Calling {func.__name__}({signature})')
    result = func(*args, **kwargs)
    print(f'{func.__name__!r} returned {result!r}')
    return result
  return wrapper

# This will execute the decorators in the order they were defined
@debug
@start_end_decorator2
def say_hello(name):
  greet = f'Hello {name}'
  print(greet)
  return greet

say_hello('Jim')





print('\n<<<<<<   Class decorator   >>>>>>')
class CountCalls:
  def __init__(self, func):
    self.func = func
    self.calls = 0

  def __call__(self, *args, **kwargs):
    self.calls += 1
    print(f'CountCalls was executed {self.calls} times!')
    return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
  print(f'Hello {name}')

say_hello('Alan')
say_hello('Jim')

'''
Just like above: 
  - a timer decorator can be used to calculate execution time of a function
  - a debug decorator can be used to print out arguments, return values, etc of a function
  - a check decorator can be used to check if the artuments fulfil requirements
  - you can also register functions, similar to plug-ins, with decorators
  - cache the return values
  - add information or update state
'''