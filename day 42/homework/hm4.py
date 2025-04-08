# 7) Create a dictionary and check if a specific key exists using the in operator.
dict1 = {
    "name": "Giorgi",
    "surname": "Kavsadze",
    "academy": "Goal-oriented-academy",
    "fav-color": "blue",
    "city": "Tbilisi"
}


user = input("Enter key: ")


if user in dict1:
    print("This key already exists!")
else:
    print("This key does not exist!")
    
