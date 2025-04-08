# 9) Add a new key-value pair to an existing dictionary and print the updated dictionary.


dict1 = {
    "name": "Giorgi",
    "surname": "Kavsadze",
    "academy": "Goal-oriented-academy",
    "fav-color": "blue",
    "city": "Tbilisi"
}


user_key = input("Enter key: ")
user_value = input("Enter value: ")


dict1[user_key] = user_value


print("Updated:", dict1)