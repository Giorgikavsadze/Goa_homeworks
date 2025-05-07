# Use map() to square each number in a list.

list1=[1,2,3,4,5,6,7,8,9,10]
square=lambda num:num**2
print(list(map(square,list1)))