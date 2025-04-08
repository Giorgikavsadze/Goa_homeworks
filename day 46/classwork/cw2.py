# Create a list comprehension that generates a list of all palindromic numbers between 10 and 200 (a palindromic number reads the same forward and backward).

list1=[i for i in range(10,201) if str(i) == str(i)[::-1]]
print(list1)