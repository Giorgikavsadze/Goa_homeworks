# Create a Python program that initializes a dictionary with at least five key-value pairs. Perform the following operations:

# Print all the keys in the dictionary using the keys() method.
# Print all the values in the dictionary using the values() method.
# Print all key-value pairs using the items() method.
# Iterate over the dictionary using the items() method and print each key with its corresponding value in a formatted string.

dict1={
    "name":"Giorgi",
    "surname":"Kavsadze",
    "academy":"Goal-oriented-academy",
    "fav-color":"blue",
    "city":"Tbilisi"
}

print(dict1.keys())
print(dict1.values())
print(dict1.items())

for key, value in dict1.items():
    print(f"{key}: {value}")