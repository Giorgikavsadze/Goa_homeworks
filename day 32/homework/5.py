# 8) Create a function that takes a string of comma-separated values (CSV) and returns a list of individual items.

def CSV(string):
    print(string.split(","))

CSV("apple,banana,orange,lemon")