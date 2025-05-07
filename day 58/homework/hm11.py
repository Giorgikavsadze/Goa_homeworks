# Use map() to subtract 5 from every element in a list.

list1=[1,2,3,4,5,6,7,8,9,10]
subtract= lambda num: num-5
print(list(map(subtract,list1)))
