# Create a list comprehension that generates a list of all numbers between 1 and 100 that are divisible by either 3 or 5, but not both.

list1=[i for i in range(1,101) if (i  % 3 == 0 or i % 5 ==0) and i%15!=0 ]
print(list1)