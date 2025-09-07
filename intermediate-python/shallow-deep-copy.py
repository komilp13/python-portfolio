'''
  - Copying mutable items
  - Difference between shallow & deep copy
    - Shallow copy: one level deep, only references of nested chile objects
    - Deep copy: full copy including chile objects; no references to orig object
  - Make copies of custom objects
'''
import copy

# Copy using assignment operator
org = 5
cpy = org    #   <- creates a reference; both vars point to same mem location

# after the above lise, the below line creates a separate memory space for the new assignment
cpy = 6

# However, for a list, that is not the case
org = [1,2]
cpy = org
cpy[0] = -10    #  <- changes the item in the original list

# to shallow copy the list
cpy_lst = copy.copy(org)   #  <- shallow copy
cpy_lst = org.copy()
cpy_lit = list(org)
cpy_lst = org[:]

# to deep copy
cpy_lst = copy.deepcopy(org)   #  <- deep copy



# Custom object copy
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person('John', 18)

# shallow copy
p2 = p1    #  <- copies the reference of the mem location
p2 = copy.copy(p1)

