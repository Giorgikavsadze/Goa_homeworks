# Use map() to multiply each number in a list by 3.

list1=[1,2,3,4,5,6,7,8,9,10]
multiply= lambda num: num*3
print(list(map(multiply,list1)))