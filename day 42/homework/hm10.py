# 13) Write a function that returns the sum of all numeric values in a dictionary.



def sum(dict1):
    total = 0
    for i in dict1.values():
        total += i
    return total

dict1 = {
    "num": 4,
    "num1": 2
}

print(sum(dict1))