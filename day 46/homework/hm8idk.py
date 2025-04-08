# 10) Create a list comprehension that finds all prime numbers between 1 and 100.

list1 = [i for i in range(2, 101) if all(i % a != 0 for a in range(2, int(i ** 0.5) + 1)) == True]
print(list1)