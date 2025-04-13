thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict.pop("model")

print(thisdict)



sample_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'country': 'USA',
    'delete_me': 'delete_me',
    'email': 'john@example.com',
    'phone': '(555) 123-4567',
    'active': True,
    'score': 85.5,
    'level': 3,
    'status': 'premium'
}

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

sample_dict.popitem()
print(sample_dict)

del sample_dict['delete_me']

print(sample_dict)

if not 'delete_me' in sample_dict: 
    print('delete_me has been removed from sample_dict')
    
fruit_dict = {
    'apple': 1,
    'banana': 2,
    'cherry': 3,
    'date': 4,
    'elderberry': 5,
    'fig': 6,
    'grape': 7,
    'honeydew': 8,
    'ice_cream_bean': 9,
    'jackfruit': 10
}

print(fruit_dict)

del fruit_dict

numbers_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

numbers_dict.clear()

print(numbers_dict)

# if not fruit_dict: 
#     print('fruit_dict has been deleted')
    

