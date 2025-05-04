# Dictionary Key Access
# Use a dictionary and try to access a key that might not exist. Handle the possible error.

dic={
    'name':"Giorgi",
    'age': 16,
    'country':"Georgia"

}

try:
    print(dic['surname'])
except KeyError:
    print("the key you are trying to reach is not in this dictionary")