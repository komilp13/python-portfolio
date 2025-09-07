'''
Errors and Exceptions
- python program will terminate when it encounters an error which could be a syntax error or exception
- Syntax errors are errors with incorrect written code - python parser will detect this and stop the code from running
- Common syntax errors: SyntaxError
- Built-in Exceptions:
    TypeError: adding two different types
    ModuleNotFoundError: importing a module that doesn't exist
    NameError: accessing a variable that doesn't exist
    FileNotFoundError: accessing file or folder that doesn't exist
    ValueError: trying to access a value in the list that doesn't exist
    IndexError: accessing index greater or smaller than the list
    KeyError: trying to access a key that doesn't exist
- Raising an exception
    use 'raise' to raise an exception
'''

# Raising an exception
x = -5
if x < 0:
  raise Exception('x should be positive')

# Raising exception using 'assert'
assert (x >= 0), 'x must be a positive number'

# Handling exceptions
try:
  x = 1 / 0
except ZeroDivisionError:
  print('division by zero exception occurred')
except:
  print('generic exception occurred')
else:
  # this gets executed when there are no exceptions
  print('no exception occurred')
finally:
  # always executes regardless if there is an exception
  #   typically used for clean up
  print('all done')


# Custom Exceptions
class ValueTooHighError(Exception):
  pass

class ValueTooLowError(Exception):
  def __init__(self, value, message):
    self.value = value
    self.message = message

def test_value(x):
  if x > 100:
    raise ValueTooHighError('Value is too high')
  elif x < 10:
    raise ValueTooLowError('Value is too low')

try:
  test_value(400)
except ValueTooHighError as e:
  print(e)
except ValueTooLowError as e:
  print(e.message + ' - ' + e.value)
