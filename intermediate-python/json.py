'''
JSON: Javascript object notation and is used in web applications
- The following was taken from https://www.python-engineer.com/learn/advancedpython11_json/
  Python type            Json type
    dict                  object
    list, tuple           array
    str                   string
    int, long, float      number
    True                  true
    False                  false
    None                  null
'''

from json import JSONEncoder
import json

person = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "hasChildren": False,
  "titles": ["engineer","programmer"]
}

# convert python obj into Json - sorts the keys alphabetically
personJson = json.dumps(person, indent=2, sort_keys=True)
print(f'serialize to json: {personJson}')

# write the python person to json
with open("person.json", "w") as json_file:
  json.dump(person, json_file, indent=2, sort_keys=True)

# convert json into python object
person = json.loads(personJson)
print(f'derserialize from json: {person}')

# read from json file
with open("person.json", "r") as json_file:
  person = json.load(json_file)
print(f'read json from file & deserialize: {person}')



# Json serialization/deserialization of custom object - method 1
class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# this function will convert a custom class to a dictionary so that it can be serialized as json
def encode_user(obj):
  if isinstance(obj, User):
    return { 'name': obj.name, 'age': obj.age, obj.__class__.__name__: True }
  else:
    raise TypeError('Object of type User is not JSON serializable')

user = User("JMAx", 27)
user_json = json.dumps(user, default=encode_user)
print(f'serialize to json [method 1]: {user_json}')


# Json serialization of custom object - method 2
class UserEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, User):
      return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    return JSONEncoder.default(self, obj)

user = User("JMAx", 27)
user_json = json.dumps(user, cls=UserEncoder)
print(f'serialize to json [method 2]: {user_json}')


# Json serialization of custom object - method 3
user = User("JMAx", 27)
user_json = UserEncoder().encode(user)
print(f'serialize to json [method 3]: {user_json}')


# deserialize the object [method 1] - the following code will create a dictionary of user properties
user = json.loads(user_json)
print(f'deserialize to python: {user}')
print(f'dserialized object type: {type(user)}')

def decode_user(dict):
  if User.__name__ in dict:
    return User(name=dict['name'], age=dict['age'])
  return dict

user = json.loads(user_json, object_hook=decode_user)
print(f'deserialize from json [method1]: {user.name}')
