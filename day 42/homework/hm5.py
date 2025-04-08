# 8) Retrieve a value from a dictionary using the get() method and handle cases where the key does not exist.

dict1 = {
    "name": "Giorgi",
    "surname": "Kavsadze",
    "academy": "Goal-oriented-academy",
    "fav-color": "blue",
    "city": "Tbilisi"
}


user = input("Enter key: ")


value = dict1.get(user, "This key does not exist!")

print(value)