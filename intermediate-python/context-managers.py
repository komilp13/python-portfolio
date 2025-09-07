'''
Context Managers: tool for resource management. They allow for allocation and releasing
  of resources when you want to. Example: 'with open' statement
'''
from contextlib import contextmanager

# file context manager - the following code will ensure that the file
#   is properly closed even if there was an exception in code
with open('test.txt', 'w') as f:
  f.write('hello world')

# without the 'with' statement, the code would look like this:
f = open('test.txt', 'w')
try:
  f.write('hello world')
finally:
  f.close()



# Custom context manager
class ManagedFile:
  def __init__(self, filename):
    print('init executed')
    self.filename = filename

  # this method will be executed as soon as the with statement is encountered
  # In this method, we want to allocate the resource & return it.
  def __enter__(self):
    print('enter executed')
    self.file = open(self.filename, 'w')
    return self.file

  # ensure that the resource is properly disposed/closed
  # the 'with' statement will return an exception if this func returns 'False'
  def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is None:
      print('got an exception')
      return False
    if self.file:
      self.file.close()
    print('exit executed')
    return True

with ManagedFile('test.txt') as f:
  f.write('hello world')




# Implementing Custom Context manager as a function
#   The below code defines a generator function and uses a decorator to
#     dco
@contextmanager
def open_managed_file(filename):
  f = open(filename, 'w')
  try:
    yield f
  finally:
    f.close()

with open_managed_file('test.txt') as f:
  f.write('hello world')




