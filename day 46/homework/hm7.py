# 9) Create a list comprehension that converts a list of temperature values in Celsius to Fahrenheit.
celsius = [0, 10, 20, 30, 40, 100]
list1 = [(i * 9/5) + 32 for i in celsius]
print(list1)