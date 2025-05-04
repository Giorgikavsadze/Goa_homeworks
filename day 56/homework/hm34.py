# 36) Create a list of numbers squared if they are divisible by 2
# Task: Use a list comprehension to create a list that squares each number in a given list only if the number is divisible by 2.

list1=[i for i in range(1,21) if i%2==0]
print(list1)